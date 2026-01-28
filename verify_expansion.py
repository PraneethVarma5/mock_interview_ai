import requests
import json

URL = "http://localhost:8000/generate_questions"

def test_auto_select():
    payload = {
        "resume_text": "Senior Software Engineer with 10 years of experience in Python, Cloud, and Team Leadership.",
        "role": "Lead Architect",
        "difficulty": "hard",
        "auto_select_count": True,
        "num_questions": 5 # Should be ignored
    }
    
    print("\n--- Testing AI Auto-Select Count ---")
    res = requests.post(URL, json=payload)
    print(f"Status: {res.status_code}")
    if res.status_code == 200:
        questions = res.json().get("questions", [])
        print(f"Questions Generated: {len(questions)}")
        if 5 <= len(questions) <= 20:
            print("PASS: AI selected a reasonable number of questions.")
        else:
            print(f"FAIL: AI selected {len(questions)} questions, which is outside 5-20 range.")
            
    # Test Max 20
    payload_max = {
        "resume_text": "Junior Dev",
        "role": "Dev",
        "num_questions": 20,
        "auto_select_count": False
    }
    print("\n--- Testing Max 20 Validation ---")
    res_max = requests.post(URL, json=payload_max)
    print(f"Status 20: {res_max.status_code}")
    if res_max.status_code != 200:
        print(f"Error: {res_max.text}")
    
    payload_err = {
        "resume_text": "Junior Dev",
        "role": "Dev",
        "num_questions": 21,
        "auto_select_count": False
    }
    res_err = requests.post(URL, json=payload_err)
    print(f"Status 21 (Should be 400): {res_err.status_code}")
    if res_err.status_code != 200:
        print(f"Error: {res_err.text}")

if __name__ == "__main__":
    test_auto_select()
