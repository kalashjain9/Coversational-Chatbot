import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API Key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

def chat_with_gemini(user_input, pdf_context=""):
    """Generate responses using Google Gemini AI."""
    context = f"Context from PDFs: {pdf_context[:2000]}" if pdf_context else "No PDFs uploaded."
    full_prompt = f"{context}\n\nUser Question: {user_input}"

    response = model.generate_content(full_prompt)
    
    # Split response into brief and long versions
    if response and response.text:
        answer = response.text.split("\n\n")
        brief_answer = answer[0] if answer else "No brief answer available."
        long_answer = "\n".join(answer[1:]) if len(answer) > 1 else "No detailed answer available."
        return brief_answer, long_answer
    else:
        return "No response.", "No response."
