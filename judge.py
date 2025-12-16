import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API Key (Expects environment variable)
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def evaluate_logic(question, model_answer, correct_answer):
    """
    Uses GPT-4o to act as a Professor.
    """
    system_prompt = """
    You are a Senior AI Research Scientist. 
    Compare the Model's Answer to the Ground Truth.
    Output a strictly formatted review:
    1. Correctness: (True/False)
    2. Reasoning Gap: Did the model hallucinate or skip a step?
    3. Critique: A short, 1-sentence explanation of the failure.
    """
    
    user_prompt = f"""
    --- QUESTION ---
    {question}
    --- GROUND TRUTH ---
    {correct_answer}
    --- MODEL GENERATED ANSWER ---
    {model_answer}
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content
