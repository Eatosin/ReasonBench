import os
import google.generativeai as genai
from dotenv import load_dotenv
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class ReasoningJudge:
    """
    Adversarial Evaluator using LLM-as-a-Judge architecture.
    Audits the reasoning path of student models against ground truth.
    """
    
    def __init__(self, model_name: str = 'gemini-2.5-flash'):
        self._configure_auth()
        try:
            self.model = genai.GenerativeModel(model_name)
        except Exception as e:
            logger.warning(f"Model {model_name} unavailable. Falling back to Pro. Error: {e}")
            self.model = genai.GenerativeModel('gemini-pro')

    def _configure_auth(self):
        """Loads API keys from environment or .env file."""
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            logger.error("GEMINI_API_KEY not found. Evaluation will fail.")
            raise ValueError("Missing API Key")
        genai.configure(api_key=api_key)

    def evaluate(self, question: str, student_answer: str, ground_truth: str) -> str:
        """
        Compares Student Answer vs Ground Truth using the Judge LLM.
        """
        prompt = f"""
        ROLE: Senior AI Research Scientist.
        TASK: Evaluate the reasoning capabilities of a candidate AI model.
        
        QUESTION:
        {question}
        
        GROUND TRUTH LOGIC:
        {ground_truth}
        
        CANDIDATE MODEL ANSWER:
        {student_answer}
        
        INSTRUCTIONS:
        Compare the logic step-by-step. 
        Output a structured review:
        1. Correctness (True/False)
        2. Reasoning Gap (Did it hallucinate or skip steps?)
        3. Critique (1-sentence technical explanation)
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"Judge Inference Failed: {e}")
            return "Error: Evaluation Failed."
