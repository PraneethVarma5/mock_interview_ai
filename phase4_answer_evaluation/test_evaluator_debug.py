import os
import sys
from dotenv import load_dotenv

# Load env before importing
load_dotenv()

try:
    from evaluator import AnswerEvaluator
except ImportError:
    # Handle running from different directories
    sys.path.append(os.path.dirname(__file__))
    from evaluator import AnswerEvaluator

def test_eval():
    print("--- Debugging Evaluator ---")
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("CRITICAL: GEMINI_API_KEY not found in env!")
    else:
        print(f"API Key found: {api_key[:5]}...")

    evaluator = AnswerEvaluator()
    try:
        print("\nSending request to Gemini...")
        result = evaluator.evaluate(
            question="Tell me about yourself.",
            answer="I am a coder."
        )
        print("\n--- Result ---")
        print(f"Score: {result.score}")
        print(f"Feedback: {result.feedback}")
        print(f"Improvements: {result.improvements}")
        
        if result.score == 5 and "unavailable" in result.feedback:
             print("\nFAILED: Fallback was triggered.")
    except Exception as e:
        print(f"\nEXCEPTION: {e}")

if __name__ == "__main__":
    test_eval()
