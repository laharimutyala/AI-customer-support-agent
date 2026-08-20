import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load model
model = genai.GenerativeModel("models/gemini-2.5-flash")


def generate_ai_response(issue: str):

    prompt = f"""
    You are a professional customer support agent.

    Customer issue:
    {issue}

    Generate a professional, polite customer support response.
    Keep the response under 80 words.
    """

    response = model.generate_content(prompt)

    return response.text