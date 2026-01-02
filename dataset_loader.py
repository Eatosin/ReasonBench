from typing import List, Dict, Any
import logging

# Configure module-level logger
logger = logging.getLogger(__name__)

def load_reasoning_data(num_samples: int = 3) -> List[Dict[str, Any]]:
    """
    Loads the GSM8K dataset (Lite Version) for reasoning evaluation.
    
    Args:
        num_samples (int): Number of tasks to load.
        
    Returns:
        List[Dict]: A list of dictionaries containing 'question' and 'answer'.
    """
    logger.info(f"Loading GSM8K Lite dataset ({num_samples} samples)...")
    
    # GSM8K Validation Samples (Hardcoded for mobile/edge compatibility)
    hard_questions = [
        {
            "question": "Natalia sold clips to 48 friends in April, and then half as many in May. How many clips did Natalia sell altogether in April and May?",
            "answer": "Natalia sold 48/2 = 24 clips in May. Natalia sold 48+24 = 72 clips altogether."
        },
        {
            "question": "Weng earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?",
            "answer": "She earns $12/60 = $0.20 per minute. So she earned $0.20 * 50 = $10."
        },
        {
            "question": "Betty is saving money for a new wallet which costs $100. Betty has only half of the money she needs. Her parents decided to give her $15 for that purpose, and her grandparents twice as much as her parents. How much more money does Betty need to buy the wallet?",
            "answer": "Betty has 100/2 = $50. Parents gave $15. Grandparents gave 15*2 = $30. Total she has = 50+15+30 = $95. She needs 100-95 = $5."
        }
    ]
    
    return hard_questions[:num_samples]
