---
description: Run the complete application (all services)
---

# Run Full Stack Application

This workflow starts all services needed for the mock interview AI application.

## Prerequisites
- Complete the setup-environment workflow first
- Ensure all dependencies are installed
- Configure your .env file with necessary API keys

## Starting All Services

You'll need to open **4 separate terminal windows** to run all services concurrently.

### Terminal 1: Frontend

1. Navigate to frontend:
   ```
   cd C:\Users\chiru\.gemini\antigravity\scratch\mock_interview_ai\phase1_frontend
   ```

2. Start the frontend:
   // turbo
   ```
   npm run dev
   ```

3. Frontend will be available at: http://localhost:3000

### Terminal 2: Resume Extraction Service

1. Navigate to resume extraction:
   ```
   cd C:\Users\chiru\.gemini\antigravity\scratch\mock_interview_ai\phase2_resume_extraction
   ```

2. Activate virtual environment:
   ```
   .\venv\Scripts\Activate.ps1
   ```

3. Start the service (if it has a server component):
   ```
   python main.py
   ```

### Terminal 3: Question Generation Service

1. Navigate to question generation:
   ```
   cd C:\Users\chiru\.gemini\antigravity\scratch\mock_interview_ai\phase3_backend_question_gen
   ```

2. Activate virtual environment:
   ```
   .\venv\Scripts\Activate.ps1
   ```

3. Start the service:
   // turbo
   ```
   python main.py
   ```

### Terminal 4: Answer Evaluation Service

1. Navigate to answer evaluation:
   ```
   cd C:\Users\chiru\.gemini\antigravity\scratch\mock_interview_ai\phase4_answer_evaluation
   ```

2. Activate virtual environment:
   ```
   .\venv\Scripts\Activate.ps1
   ```

3. Start the service:
   // turbo
   ```
   python evaluator.py
   ```

## Verification

Once all services are running:
1. Open http://localhost:3000 in your browser
2. Test the resume upload functionality
3. Verify question generation works
4. Test the answer evaluation feature

## Stopping All Services

To stop all services:
- Press `Ctrl+C` in each terminal window
- Deactivate Python virtual environments if needed

## Notes
- Services must be started in order if there are dependencies
- Check each terminal for error messages
- Ensure ports are not already in use
- All services should show "running" or "listening" status before testing
