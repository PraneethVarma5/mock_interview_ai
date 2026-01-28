from pydantic import BaseModel
from typing import List, Dict
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class EvaluationResult(BaseModel):
    score: int  # 0-10
    feedback: str
    missing_keywords: List[str]
    improvements: str = ""
    ideal_answer: str = ""  # The "sample/ideal" answer

class AnswerEvaluator:
    def __init__(self):
        # In a real app, this would load models or connect to LLM
        pass
    
    def evaluate(self, question: str, answer: str, context_keywords: List[str] = []) -> EvaluationResult:
        # Check for empty or placeholder answers
        if not answer or answer.strip() == "" or "no answer provided" in answer.lower():
            print("Answer is empty or placeholder. Skipping AI evaluation.")
            return EvaluationResult(
                score=0,
                feedback="This question was not answered or skipped.",
                missing_keywords=[],
                improvements="Please provide a detailed response to receive feedback.",
                ideal_answer="A good answer would address the specific technical or behavioral aspects of the question."
            )

        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
             print("Warning: GEMINI_API_KEY not found, using fallback evaluation.")
             return self._fallback_evaluate(question, answer, context_keywords, "API Key missing")
             
        genai.configure(api_key=api_key)
        
        # Try these models in order
        candidate_models = [
            'gemini-2.0-flash',
            'gemini-flash-latest',
            'gemini-2.5-flash-lite'
        ]
        
        last_error = None

        for model_name in candidate_models:
            try:
                print(f"Attempting evaluation with {model_name}...")
                model = genai.GenerativeModel(model_name)
                
                prompt = f"""
                You are an expert technical interviewer. Evaluate the following answer to the question provided.
                
                Question: {question}
                Answer: {answer}
                Context Keywords (optional): {', '.join(context_keywords)}
                
                INSTRUCTIONS:
                - If the question is a "coding" question, evaluate the code for logic, correctness, efficiency, and clarity.
                - If the question is "behavioral" or "technical", evaluate based on relevance, depth, and communication.
                - Provide a score (0-10) and CONCISE, SIMPLE feedback (max 2 sentences).
                - For coding questions, be specific about potential bugs or better approaches.
                - ALSO provide specific, brief "improvements" on how to make the answer better.
                - FINALLY, provide a highly professional, concise "ideal_answer" (max 3 sentences) that demonstrates the perfect response to this question. For coding questions, provide the optimized code.
                
                Output ONLY a valid JSON object with keys: 
                - "score" (int)
                - "feedback" (string)
                - "missing_keywords" (list of strings)
                - "improvements" (string)
                - "ideal_answer" (string)
                """
                
                response = model.generate_content(prompt)
                text = response.text.strip()
                
                # Robust cleanup
                if text.startswith("```json"):
                    text = text[7:]
                if text.startswith("```"):
                    text = text[3:]
                if text.endswith("```"):
                    text = text[:-3]
                text = text.strip()
                
                import json
                try:
                    data = json.loads(text)
                except json.JSONDecodeError:
                    # Last resort cleanup
                    start = text.find("{")
                    end = text.rfind("}") + 1
                    if start != -1 and end != -1:
                        data = json.loads(text[start:end])
                    else:
                        raise ValueError("Could not parse JSON from LLM response")
                
                return EvaluationResult(
                    score=data.get("score", 0),
                    feedback=data.get("feedback", "No feedback provided."),
                    missing_keywords=data.get("missing_keywords", []),
                    improvements=data.get("improvements", "No specific improvements suggested."),
                    ideal_answer=data.get("ideal_answer", "No ideal answer provided.")
                )
            except Exception as e:
                print(f"Model {model_name} failed: {e}")
                last_error = e
                # Continue to next model
        
        return self._fallback_evaluate(question, answer, context_keywords, str(last_error))

    def _fallback_evaluate(self, question: str, answer: str, context_keywords: List[str], error_msg: str = "") -> EvaluationResult:
        # Original simple logic
        score = 5
        feedback = f"Evaluation service unavailable. Error: {error_msg}"
        return EvaluationResult(score=score, feedback=feedback, missing_keywords=[], improvements="Check API Quota or Connection.")

if __name__ == "__main__":
    # Test logic
    evaluator = AnswerEvaluator()
    res = evaluator.evaluate(
        "What is React?", 
        "React is a JavaScript library for building user interfaces.", 
        ["library", "javascript", "interface"]
    )
    print(f"Score: {res.score}")
    print(f"Feedback: {res.feedback}")
