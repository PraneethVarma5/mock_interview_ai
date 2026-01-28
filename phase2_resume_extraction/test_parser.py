import os
from resume_parser import parse_resume

def test_txt_parser():
    # Create a dummy file
    filename = "test_resume.txt"
    with open(filename, "w") as f:
        f.write("John Doe\nSoftware Engineer\nSkills: Python, React")
    
    try:
        data = parse_resume(filename)
        print(f"Successfully parsed {filename}")
        print(f"Extracted Text: {data.text}")
        assert "John Doe" in data.text
    finally:
        if os.path.exists(filename):
            os.remove(filename)

if __name__ == "__main__":
    test_txt_parser()
