import pandas as pd
from datasets import load_dataset

def load_reasoning_data(num_samples=10):
    """
    Loads the GSM8K dataset (hard math problems).
    """
    print(f"📊 Loading GSM8K dataset (Top {num_samples} samples)...")
    dataset = load_dataset("gsm8k", "main", split="test")
    df = pd.DataFrame(dataset)
    sample_batch = df.head(num_samples).to_dict('records')
    print(f"✅ Loaded {len(sample_batch)} reasoning tasks.")
    return sample_batch

if __name__ == "__main__":
    data = load_reasoning_data(5)
    print("Example Question:", data[0]['question'])
