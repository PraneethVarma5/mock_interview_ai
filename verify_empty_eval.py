from phase4_answer_evaluation.evaluator import AnswerEvaluator

def test_empty_answer():
    evaluator = AnswerEvaluator()
    
    print("\n--- Testing Empty Answer ---")
    res = evaluator.evaluate("What is Python?", "")
    print(f"Score: {res.score}")
    print(f"Feedback: {res.feedback}")
    assert res.score == 0
    assert "not answered" in res.feedback
    
    print("\n--- Testing Placeholder Answer ---")
    res2 = evaluator.evaluate("What is React?", "No answer provided.")
    print(f"Score: {res2.score}")
    print(f"Feedback: {res2.feedback}")
    assert res2.score == 0
    assert "not answered" in res2.feedback
    
    print("\n--- Testing Actual Answer (Should still use AI if key exists, or fallback) ---")
    # Note: If no API key, this will return the fallback result with score 5
    res3 = evaluator.evaluate("What is HTML?", "A markup language for web pages.")
    print(f"Score: {res3.score}")
    print(f"Feedback: {res3.feedback}")

if __name__ == "__main__":
    test_empty_answer()
