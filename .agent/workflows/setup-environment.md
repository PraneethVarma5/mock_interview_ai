---
description: Initial setup for the entire project
---

# Setup Development Environment

Follow these steps to set up the complete mock interview AI project:

## Prerequisites

Ensure you have the following installed:
- Node.js (v18 or higher)
- Python (v3.8 or higher)
- Git

## Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd C:\Users\chiru\.gemini\antigravity\scratch\mock_interview_ai\phase1_frontend
   ```

2. Install Node.js dependencies:
   // turbo
   ```
   npm install
   ```

## Backend Setup (All Phases)

### Phase 2: Resume Extraction

1. Navigate to the resume extraction directory:
   ```
   cd C:\Users\chiru\.gemini\antigravity\scratch\mock_interview_ai\phase2_resume_extraction
   ```

2. Create virtual environment:
   ```
   python -m venv venv
   ```

3. Activate virtual environment:
   ```
   .\venv\Scripts\Activate.ps1
   ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Phase 3: Question Generation

1. Navigate to the question generation directory:
   ```
   cd C:\Users\chiru\.gemini\antigravity\scratch\mock_interview_ai\phase3_backend_question_gen
   ```

2. Create virtual environment:
   ```
   python -m venv venv
   ```

3. Activate virtual environment:
   ```
   .\venv\Scripts\Activate.ps1
   ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Phase 4: Answer Evaluation

1. Navigate to the answer evaluation directory:
   ```
   cd C:\Users\chiru\.gemini\antigravity\scratch\mock_interview_ai\phase4_answer_evaluation
   ```

2. Create virtual environment:
   ```
   python -m venv venv
   ```

3. Activate virtual environment:
   ```
   .\venv\Scripts\Activate.ps1
   ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Environment Variables

1. Copy the example environment file:
   ```
   cd C:\Users\chiru\.gemini\antigravity\scratch\mock_interview_ai
   cp .env.example .env
   ```

2. Edit the `.env` file and add your API keys and configuration:
   - Add your AI/LLM API keys
   - Configure any database connections
   - Set up any other required environment variables

## Verification

After setup, verify each component:
- Run the frontend: `npm run dev` in phase1_frontend
- Test resume extraction: `python test_parser.py` in phase2_resume_extraction
- Test question generation: `python main.py` in phase3_backend_question_gen
- Test answer evaluation: `python evaluator.py` in phase4_answer_evaluation

## Notes
- Each Python phase has its own virtual environment to avoid dependency conflicts
- Make sure to activate the appropriate virtual environment before working on each phase
- Keep your .env file secure and never commit it to version control
