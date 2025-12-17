import pandas as pd
from tqdm import tqdm
from dataset_loader import load_reasoning_data
# Import the new Gemini functions
from judge import evaluate_logic, get_gemini_response 

def solve_problem(question):
    """
    The 'Student' model attempts to solve the problem.
    We ask it to think step-by-step.
    """
    prompt = f"Solve this math problem step-by-step: {question}"
    return get_gemini_response(prompt)

def run_experiment():
    # Load just 2 questions to test if it works fast
    tasks = load_reasoning_data(num_samples=2)
    results = []

    print("\n🔬 Starting ReasonBench Experiment (Powered by Gemini)...\n")

    for task in tqdm(tasks):
        question = task['question']
        ground_truth = task['answer']
        
        # 1. Student tries to solve it
        student_answer = solve_problem(question)
        
        # 2. Professor grades it
        evaluation = evaluate_logic(question, student_answer, ground_truth)
        
        results.append({
            "Question": question,
            "Student_Answer": student_answer,
            "Ground_Truth": ground_truth,
            "Evaluation": evaluation
        })

    # Save results
    df = pd.DataFrame(results)
    df.to_csv("experiment_results.csv", index=False)
    print("\n✅ Experiment Complete! Results saved to 'experiment_results.csv'")

if __name__ == "__main__":
    run_experiment()