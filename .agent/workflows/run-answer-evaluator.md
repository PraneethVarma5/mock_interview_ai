---
description: How to run the answer evaluation service
---

# Run Answer Evaluation Service

Follow these steps to start the answer evaluation service:

1. Navigate to the answer evaluation directory:
   ```
   cd C:\Users\chiru\.gemini\antigravity\scratch\mock_interview_ai\phase4_answer_evaluation
   ```

2. Activate the virtual environment (if not already active):
   ```
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies (if not already installed):
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables (ensure .env is configured):
   ```
   cp ..\.env.example .env
   ```

5. Run the evaluator service:
   // turbo
   ```
   python evaluator.py
   ```

## Notes
- Ensure your API keys are properly configured in the .env file
- The evaluator uses AI models to assess candidate responses
- Check the service logs for any errors or warnings
