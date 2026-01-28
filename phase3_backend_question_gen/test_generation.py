import os
import sys

# Add the parent directory to sys.path to ensure module resolution works if run from subfolder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from phase3_backend_question_gen.question_generator import QuestionGenerator

def test_generation():
    print("Initializing Question Generator...")
    try:
        generator = QuestionGenerator()
    except ValueError as e:
        print(f"Initialization failed: {e}")
        return

    # Dummy resume text for testing
    dummy_resume = """
    Jane Doe
    Software Engineer with 5 years of experience.
    Skills: Python, AWS, Docker, Kubernetes, FastApi, PostgreSQL.
    Experience:
    - Built a microservices architecture for a fintech startup using Python and FastAPI.
    - Optimized database queries in PostgreSQL reducing load times by 40%.
    - Deployed applications using Docker and Kubernetes on AWS.
    Education: B.S. in Computer Science.
    """
    
    print("\nDrafting questions for: Senior Python Developer")
    questions = generator.generate_questions(dummy_resume, role="Senior Python Developer", num_questions=3)
    
    if not questions:
        print("No questions were generated.")
        return

    print(f"\nSuccessfully generated {len(questions)} questions:\n")
    for q in questions:
        print(f"[{q.get('type', 'general').upper()}] ({q.get('difficulty', 'unknown')})")
        print(f"Q: {q.get('text')}")
        print(f"Context: {q.get('context')}")
        print("-" * 40)

if __name__ == "__main__":
    test_generation()
