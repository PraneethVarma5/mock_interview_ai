---
description: How to test the resume extraction module
---

# Test Resume Extraction

Follow these steps to test the resume extraction functionality:

1. Navigate to the resume extraction directory:
   ```
   cd C:\Users\chiru\.gemini\antigravity\scratch\mock_interview_ai\phase2_resume_extraction
   ```

2. Activate the virtual environment (if not already active):
   ```
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies (if not already installed):
   ```
   pip install -r requirements.txt
   ```

4. Run the test parser:
   // turbo
   ```
   python test_parser.py
   ```

5. Review the output to verify resume parsing is working correctly

## Testing with Custom Resume

To test with a different resume file:

1. Place your resume file in the project root or specify the path
2. Update the file path in `test_parser.py` if needed
3. Run the test again

## Notes
- Supported formats: PDF, DOCX, TXT
- Check the output for extracted skills, experience, and education
- Verify that the extraction accuracy meets your requirements
