import requests
import json
import time

URL = "http://localhost:8000/generate_questions"

def test_caching_and_fallback():
    payload = {
        "resume_text": "Experienced Python Developer with skills in Django and React.",
        "role": "Software Engineer",
        "num_questions": 3,
        "difficulty": "medium"
    }
    
    # 1. First Call (May hit AI or Cache)
    print("\n--- Call 1: Checking Cache/AI ---")
    start = time.time()
    res1 = requests.post(URL, json=payload)
    end = time.time()
    print(f"Status: {res1.status_code}")
    print(f"Time: {end - start:.2f}s")
    
    # 2. Second Call (Should definitely hit Cache and be faster)
    print("\n--- Call 2: Verifying Cache (Should be < 0.5s) ---")
    start = time.time()
    res2 = requests.post(URL, json=payload)
    end = time.time()
    print(f"Status: {res2.status_code}")
    print(f"Time: {end - start:.2f}s")
    
    if (end - start) < 0.5:
        print("PASS: Caching is working correctly.")
    else:
        print("FAIL: Caching might not be working as expected.")

    # 3. Test Static Fallback (Simulate by sending garbage that might fail but we catch it)
    # Actually, to truly test static fallback, we'd need to simulate a 429.
    # But we can verify the get_fallback_questions logic works.
    print("\n--- Verifying Fallback Logic (Mocking empty response) ---")
    from phase3_backend_question_gen.question_bank import get_fallback_questions
    fallback = get_fallback_questions("Python Developer", 2)
    print(f"Fallback Questions Count: {len(fallback)}")
    if len(fallback) == 2 and "Python" in str(fallback):
        print("PASS: Static bank fallback logic is sound.")
    else:
        print("FAIL: Static bank fallback logic issue.")

if __name__ == "__main__":
    test_caching_and_fallback()
