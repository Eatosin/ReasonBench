import pandas as pd
from tqdm import tqdm
from dataset_loader import load_reasoning_data
from judge import evaluate_logic, client

def solve_problem(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Solve this math problem step-by-step."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

def run_experiment():
    tasks = load_reasoning_data(num_samples=3)
    results = []
    print("\n🔬 Starting ReasonBench Experiment...\n")

    for task in tqdm(tasks):
        question = task['question']
        ground_truth = task['answer']
        student_answer = solve_problem(question)
        evaluation = evaluate_logic(question, student_answer, ground_truth)
        
        results.append({
            "Question": question,
            "Student_Answer": student_answer,
            "Ground_Truth": ground_truth,
            "Evaluation": evaluation
        })

    df = pd.DataFrame(results)
    df.to_csv("experiment_results.csv", index=False)
    print("\n✅ Experiment Complete! Results saved to 'experiment_results.csv'")

if __name__ == "__main__":
    run_experiment()
