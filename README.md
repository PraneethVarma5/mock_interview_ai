# 🎯 AI Mock Interview Coach

A comprehensive, AI-powered platform to help job seekers practice interviews. It analyzes your resume, generates tailored technical and behavioral questions using Google's Gemini LLM, and provides detailed feedback on your answers.

---

## 🚀 How it Works (The Workflow)

1.  **📄 Upload Resume**: Upload your resume (PDF/TXT). The system extracts your skills and experience.
2.  **⚙️ Customize**: Choose difficulty (Easy to Hard) and the number of questions. Optionally add a Job Description.
3.  **🎤 Interview**: Face real-time AI-generated questions based on *your* background.
4.  **📊 Feedback**: Get a score out of 10 and detailed advice on how to improve each answer.

---

## 🏗️ Project Structure

The project is divided into 4 clear phases:

| Phase | Component | Responsibility |
| :--- | :--- | :--- |
| **Phase 1** | `phase1_frontend` | **The UI**: Built with Next.js, React, and Tailwind CSS. |
| **Phase 2** | `phase2_resume_extraction` | **The Parser**: Python scripts that read and extract text from resumes. |
| **Phase 3** | `phase3_backend_question_gen` | **The Brain**: FastAPI server that talks to Gemini AI to generate questions. |
| **Phase 4** | `phase4_answer_evaluation` | **The Critic**: Evaluates user answers and provides scores/feedback. |

---

## 🛠️ Getting Started

### 1. Prerequisites
- **Node.js**: (for Frontend)
- **Python 3.10+**: (for Backend)
- **Gemini API Key**: Get one from [Google AI Studio](https://aistudio.google.com/).

### 2. Setup Backend
```bash
cd phase3_backend_question_gen
pip install -r requirements.txt
# Create a .env file with: GOOGLE_API_KEY=your_key_here
python main.py
```
*Backend runs on: http://localhost:8000*

### 3. Setup Frontend
```bash
cd phase1_frontend
npm install
npm run dev
```
*Frontend runs on: http://localhost:3000*

---

## 🧠 Technologies Used
- **Frontend**: Next.js, TypeScript, Tailwind CSS, Lucide Icons.
- **Backend**: FastAPI (Python), Uvicorn.
- **AI**: Google Generative AI (Gemini Pro).
- **Libraries**: Pydantic, Dotenv, PyPDF2 (likely in Phase 2).

---

## 💡 Key Features
- **Dynamic Question Generation**: Questions change every time based on your resume.
- **Context-Aware Evaluation**: The AI knows what you *should* have said based on your experience.
- **Premium UI**: Sleek dark mode with smooth animations and progress tracking.
