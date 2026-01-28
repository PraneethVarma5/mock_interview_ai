import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def test_api():
    with open("result.txt", "w") as f:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            f.write("Error: GEMINI_API_KEY not found in .env\n")
            return
        
        if "your_api_key" in api_key:
            f.write("Error: API Key is still the placeholder text.\n")
            return

        f.write(f"Found API Key: {api_key[:5]}...{api_key[-3:]}\n")
        
        try:
            genai.configure(api_key=api_key)
            f.write("Listing available models:\n")
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods:
                    f.write(f"- {m.name}\n")
            
            f.write("Attempting generation with gemini-2.0-flash-exp...\n")
            try:
                model = genai.GenerativeModel('gemini-2.0-flash-exp')
                response = model.generate_content("Say 'Hello, AI Interviewer!'")
                f.write(f"API Response (2.0): {response.text}\n")
            except:
                f.write("gemini-2.0-flash-exp failed. Trying gemini-1.5-flash...\n")
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content("Say 'Hello, AI Interviewer!'")
                f.write(f"API Response (1.5): {response.text}\n")
                
        except Exception as e:
            f.write(f"API Connection Failed: {e}\n")

if __name__ == "__main__":
    test_api()
