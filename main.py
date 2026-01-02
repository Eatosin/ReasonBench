import pandas as pd
import logging
from tqdm import tqdm
from dataset_loader import load_reasoning_data
from judge import ReasoningJudge
import google.generativeai as genai

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("ReasonBench")

def solve_problem(model, question: str) -> str:
    """
    Simulates the 'Student' model attempting to solve the problem.
    """
    prompt = f"Solve this math problem step-by-step: {question}"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        logger.error(f"Student Model Error: {e}")
        return "Error"

def run_experiment():
    """
    Executes the main evaluation loop: Load -> Solve -> Judge -> Save.
    """
    # 1. Setup
    judge = ReasoningJudge()
    student_model = genai.GenerativeModel('gemini-2.5-flash') # Or 'gemini-pro' if 2.5 unavailable
    
    tasks = load_reasoning_data(num_samples=3)
    results = []

    logger.info("🔬 Starting ReasonBench Experiment...")

    # 2. Evaluation Loop
    for task in tqdm(tasks, desc="Evaluating"):
        question = task['question']
        ground_truth = task['answer']
        
        # Student Attempt
        student_answer = solve_problem(student_model, question)
        
        # Adversarial Judgment
        evaluation = judge.evaluate(question, student_answer, ground_truth)
        
        results.append({
            "Question": question,
            "Student_Answer": student_answer,
            "Ground_Truth": ground_truth,
            "Evaluation": evaluation
        })

    # 3. Save Artifacts
    df = pd.DataFrame(results)
    output_file = "experiment_results.csv"
    df.to_csv(output_file, index=False)
    logger.info(f"✅ Experiment Complete. Results saved to {output_file}")

if __name__ == "__main__":
    run_experiment()
