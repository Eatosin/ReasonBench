import pandas as pd

def load_reasoning_data(num_samples=3):
    """
    Returns a manual list of hard math problems (GSM8K Lite)
    Optimized for lightweight execution.
    """
    print(f"📊 Loading Lite Dataset ({num_samples} samples)...")
    
    # GSM8K Validation Samples
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

if __name__ == "__main__":
    data = load_reasoning_data(1)
    print("Example:", data[0]['question'])