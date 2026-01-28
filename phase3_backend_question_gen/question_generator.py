import os
import json
import typing_extensions
import google.generativeai as genai
from dotenv import load_dotenv

# Use TypedDict for schema definition as it's often more reliable for simple JSON constraints with Gemini
class Question(typing_extensions.TypedDict):
    id: int
    text: str
    type: str  # "technical" | "behavioral" | "coding"
    difficulty: str # "easy" | "medium" | "hard"
    context: str
    initial_code: typing_extensions.NotRequired[str] # Recommended boiler-plate code for coding questions

class InterviewScript(typing_extensions.TypedDict):
    questions: list[Question]

class QuestionGenerator:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        # Using a model that supports JSON mode well
        self.model = genai.GenerativeModel('gemini-flash-latest',
                                           generation_config={"response_mime_type": "application/json"})

    def generate_questions(self, resume_text: str, role: str = "Software Engineer", num_questions: int = 5, difficulty: str = "mixed", job_description: str = "", auto_select_count: bool = False) -> list[Question]:
        """
        Generates interview questions based on the provided resume text and target role.
        """
        
        # Build difficulty instruction
        if difficulty == "mixed":
            difficulty_instruction = "Mix of easy, medium, and hard questions."
        else:
            difficulty_instruction = f"All questions should be {difficulty} difficulty level."
        
        # Build quantity instruction
        if auto_select_count:
            quantity_instruction = "Decide on an optimal number of interview questions (between 5 and 20) based on the depth of the resume and the complexity of the job description. Aim for a comprehensive evaluation."
        else:
            quantity_instruction = f"Generate exactly {num_questions} interview questions."

        # Build job description section
        job_desc_section = "None provided."
        if job_description.strip():
            job_desc_section = f"---\n{job_description[:2000]}\n---"
        
        prompt = f"""
        You are an expert technical and HR interviewer. 
        Your goal is to conduct a thorough interview for a candidate applying for a {role} position.
        
        {quantity_instruction}
        
        CANDIDATE DATA:
        Resume Content:
        ---
        {resume_text}
        ---
        Job Description:
        {job_desc_section}
        
        REQUIRED MIX OF QUESTIONS (CRITICAL):
        1. **Resume-Deep Dive (40%)**: Specific technical questions & behavioral scenarios based on the projects/skills in their resume.
        2. **JD-Alignment (30%)**: Target requirements in the Job Description, even if not on the resume. Ask how they'd adapt their current skills to these new core requirements.
        3. **Industry Standards (20%)**: Realistic "must-know" questions for a {role} (e.g., system design, core principles, patterns).
        4. **HR & Behavioral (10%)**: Standard soft-skill questions (conflict, growth, culture fit).
        
        STRICT RULES:
        - **Zero Hallucination**: Do NOT invent projects or specific companies the candidate hasn't listed.
        - **Experience Lock**: For "Resume-Deep Dive" questions, only use their actual listed tech/projects.
        - **JD Flexibility**: It is OK (and required) to ask about JD skills they haven't listed yet to test their adaptability and learning curve.
        - **Context Field**: For EVERY question, state the category (Resume, JD, Industry, or HR) and the specific reason/source for asking.
        - {difficulty_instruction}
        - Each question must be realistic and high-impact.
        
        RESPONSE FORMAT:
        For each question, provide:
        - id: A unique number
        - text: The question text
        - type: "technical", "behavioral", or "coding"
        - difficulty: "easy", "medium", or "hard"
        - context: "[Category] Reason for this question: (quote/cite if applicable)"
        - initial_code: (For "coding" type only) A simple boilerplate snippet.
        
        Return a JSON object with a single key "questions" containing these objects.
        """

        candidate_models = [
            'gemini-2.5-flash',
            'gemini-2.0-flash',
            'gemini-flash-latest',
            'gemini-2.5-flash-lite'
        ]
        
        last_error = None
        for model_name in candidate_models:
            try:
                print(f"Generating questions with model: {model_name}")
                model = genai.GenerativeModel(model_name, generation_config={"response_mime_type": "application/json"})
                response = model.generate_content(prompt)
                
                # Handle empty response
                if not response.text:
                    continue
                    
                data = json.loads(response.text)
                
                # Simple validation to ensure we got what we expected
                if "questions" in data:
                    return data["questions"]
                elif isinstance(data, list):
                    return data
                else:
                    print(f"Unexpected JSON structure from {model_name}: {data.keys()}")
                    continue
                     
            except Exception as e:
                print(f"Error with {model_name}: {e}")
                last_error = e
                # Continue and try the next model
        
        # If we reach here, all models failed
        if last_error:
            raise last_error
        return []

if __name__ == "__main__":
    # Quick sanity check
    gen = QuestionGenerator()
    params = {"resume_text": "Experience with Python, Django, and React.", "role": "Full Stack Dev"}
    # We won't actually call the API here to save quota during import/tests unless explicitly run
    print("QuestionGenerator initialized.")
