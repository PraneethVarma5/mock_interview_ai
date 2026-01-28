from typing import List, Dict, Any

# A static collection of high-quality interview questions for common stacks
# This serves as the Level 3 (Final) fallback when all AI models hit quota limits.

QUESTION_BANK: Dict[str, List[Dict[str, Any]]] = {
    "python": [
        {
            "id": 1001,
            "text": "Explain the difference between a list and a tuple in Python. When would you use one over the other?",
            "type": "technical",
            "difficulty": "easy",
            "context": "Core Python proficiency.",
            "initial_code": ""
        },
        {
            "id": 1002,
            "text": "What are Python decorators and how do they work? Provide a simple use case.",
            "type": "technical",
            "difficulty": "medium",
            "context": "Advanced Python concepts.",
            "initial_code": ""
        },
        {
            "id": 1003,
            "text": "Write a function that takes a string and returns it reversed. Example: 'hello' -> 'olleh'.",
            "type": "coding",
            "difficulty": "easy",
            "context": "Basic algorithmic thinking in Python.",
            "initial_code": "def reverse_string(s):\n    # Your code here\n    pass"
        }
    ],
    "javascript": [
        {
            "id": 2001,
            "text": "What is the difference between '==' and '===' in JavaScript?",
            "type": "technical",
            "difficulty": "easy",
            "context": "JS fundamentals.",
            "initial_code": ""
        },
        {
            "id": 2002,
            "text": "Explain the concept of 'closures' in JavaScript with an example.",
            "type": "technical",
            "difficulty": "medium",
            "context": "Scope and memory management in JS.",
            "initial_code": ""
        },
        {
            "id": 2003,
            "text": "Write a function that filters an array of numbers to return only the even ones.",
            "type": "coding",
            "difficulty": "easy",
            "context": "Array manipulation in JS.",
            "initial_code": "function filterEvens(arr) {\n    // Your code here\n}"
        }
    ],
    "react": [
        {
            "id": 3001,
            "text": "What are React Hooks? Explain useState and useEffect.",
            "type": "technical",
            "difficulty": "easy",
            "context": "Modern React development.",
            "initial_code": ""
        },
        {
            "id": 3002,
            "text": "What is the Virtual DOM, and how does React use it to improve performance?",
            "type": "technical",
            "difficulty": "medium",
            "context": "React architecture.",
            "initial_code": ""
        }
    ],
    "general_behavioral": [
        {
            "id": 4001,
            "text": "Tell me about a challenging project you worked on. What were the obstacles and how did you overcome them?",
            "type": "behavioral",
            "difficulty": "medium",
            "context": "Problem-solving and resilience.",
            "initial_code": ""
        },
        {
            "id": 4002,
            "text": "Where do you see yourself in two years in terms of your career growth?",
            "type": "behavioral",
            "difficulty": "easy",
            "context": "Ambition and career alignment.",
            "initial_code": ""
        },
        {
            "id": 4003,
            "text": "How do you handle disagreement with a teammate or supervisor?",
            "type": "behavioral",
            "difficulty": "easy",
            "context": "Conflict resolution and teamwork.",
            "initial_code": ""
        }
    ]
}

def get_fallback_questions(resume_text: str, num_questions: int = 5) -> List[Dict[str, Any]]:
    """
    Detects skills from resume text and pulls matching questions from the bank.
    Always includes at least one behavioral question.
    """
    resume_lower = resume_text.lower()
    selected = []
    
    # 1. Detect technical matches
    for skill, questions in QUESTION_BANK.items():
        if skill != "general_behavioral" and skill in resume_lower:
            selected.extend(questions)
            
    # 2. Add behavioral if we have space
    selected.extend(QUESTION_BANK["general_behavioral"])
    
    # 3. Unique IDs and Limit
    seen_ids = set()
    unique_selected = []
    for q in selected:
        if q["id"] not in seen_ids:
            unique_selected.append(q)
            seen_ids.add(q["id"])
            
    # 4. Fallback if empty (e.g. no skills detected)
    if not unique_selected:
        unique_selected = QUESTION_BANK["general_behavioral"]
        
    return unique_selected[:num_questions]
