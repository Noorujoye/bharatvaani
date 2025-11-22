import os
from dotenv import load_dotenv
import google.generativeai as genai
from .prompts import SYSTEM_PROMPT

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=SYSTEM_PROMPT
)

def generate_response(query: str):
    try:
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        return f"⚠️ Model Error: {e}"
