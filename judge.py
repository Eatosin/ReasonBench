import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Load the Secret Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ Error: GEMINI_API_KEY not found in .env file")

# 2. Configure Google Gemini
genai.configure(api_key=api_key)

# We use 'gemini-1.5-flash' because it is fast, free, and smart.
model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(prompt):
    """
    Helper function to talk to Gemini
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def evaluate_logic(question, model_answer, correct_answer):
    """
    Uses Gemini to act as the Professor/Judge.
    """
    prompt = f"""
    You are a Senior AI Research Scientist. 
    Evaluate the Candidate's reasoning based on the Ground Truth.
    
    --- QUESTION ---
    {question}
    
    --- GROUND TRUTH ---
    {correct_answer}
    
    --- CANDIDATE ANSWER ---
    {model_answer}
    
    Output a strictly formatted review:
    1. Correctness: (True/False)
    2. Reasoning Gap: Did the model hallucinate or skip a step?
    3. Critique: A short explanation of the failure.
    """
    
    return get_gemini_response(prompt)