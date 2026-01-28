---
description: How to run the question generation backend
---

# Run Question Generation Backend

Follow these steps to start the question generation service:

1. Navigate to the question generation directory:
   ```
   cd C:\Users\chiru\.gemini\antigravity\scratch\mock_interview_ai\phase3_backend_question_gen
   ```

2. Create a virtual environment (if not already created):
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   ```
   .\venv\Scripts\Activate.ps1
   ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Set up environment variables (copy .env.example to .env and configure):
   ```
   cp ..\.env.example .env
   ```

6. Run the question generation service:
   // turbo
   ```
   python main.py
   ```

## Notes
- Ensure you have Python 3.8+ installed
- Make sure to configure your API keys in the .env file
- The service will typically run on port 8000 or as configured
