import sys
import os
import json

# Add Phase 3 to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'phase3_backend_question_gen')))
from question_generator import QuestionGenerator

def verify_zero_hallucination():
    gen = QuestionGenerator()
    
    # SCENARIO: No Experience, only Python skill
    resume_text = """
    Name: John Doe
    Education: BS in Computer Science (2025 Expected)
    Skills: Python, SQL, Algorithms
    Projects: 
    - Personal Portfolio: A website built with Python and Flask.
    - Sorting Algorithm Visualizer: Python-based visualizer for quicksort.
    """
    
    print("\n--- Testing Zero Hallucination (Fresh Grad, Python Only) ---")
    questions = gen.generate_questions(resume_text, role="Software Engineer", num_questions=4, difficulty="easy")
    
    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1} [{q.get('type')}]:")
        print(f"Text: {q.get('text')}")
        print(f"Context: {q.get('context')}")
        if q.get('type') == 'coding':
            print(f"Initial Code: \n{q.get('initial_code')}")
            
    # Check for hallucinations
    js_found = any("javascript" in (q.get('text', '') + q.get('initial_code', '')).lower() for q in questions)
    exp_found = any("past role" in q.get('text', '').lower() or "previous job" in q.get('text', '').lower() for q in questions)
    
    if js_found:
        print("\nFAIL: Found JavaScript in questions despite resume only listing Python.")
    else:
        print("\nPASS: No language hallucination detected.")
        
    if exp_found:
        print("FAIL: Found 'past role/job' phrasing despite resume having no work experience.")
    else:
        print("PASS: Experience awareness detected (no professional role hallucinations).")

if __name__ == "__main__":
    verify_zero_hallucination()
