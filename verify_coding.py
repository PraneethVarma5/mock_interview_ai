import sys
import os
import json

# Add Phase 3 to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'phase3_backend_question_gen')))
from question_generator import QuestionGenerator

def verify_coding_questions():
    gen = QuestionGenerator()
    resume_text = "Experienced Senior Python Backend Engineer with 5 years in Django, FastAPI, and PostgreSQL. Proficient in algorithms and data structures."
    
    print("Generating questions...")
    questions = gen.generate_questions(resume_text, role="Senior Python Developer", num_questions=5, difficulty="mixed")
    
    coding_questions = [q for q in questions if q.get('type') == 'coding']
    
    print(f"Generated {len(questions)} total questions.")
    print(f"Found {len(coding_questions)} coding questions.")
    
    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1} [{q.get('type')}]:")
        print(f"Text: {q.get('text')}")
        if q.get('type') == 'coding':
            print(f"Initial Code: \n{q.get('initial_code')}")
            
    if len(coding_questions) > 0:
        print("\nSUCCESS: Coding questions generated correctly.")
    else:
        print("\nWARNING: No coding questions generated. Refine prompt if necessary.")

if __name__ == "__main__":
    verify_coding_questions()
