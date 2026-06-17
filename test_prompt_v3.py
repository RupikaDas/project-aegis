from src.ingestion.load_data import load_csv

from src.prompt_engineering.prompt_simulator import (
    simulate_prompt_v3
)

from src.evaluation.evaluation_metrics import (
    calculate_accuracy,
    calculate_precision,
    calculate_recall,
    calculate_f1
)

df = load_csv(
    "data/raw/train.csv"
)

results = simulate_prompt_v3(df)

accuracy = calculate_accuracy(results)

precision = calculate_precision(results)

recall = calculate_recall(results)

f1 = calculate_f1(
    precision,
    recall
)

print()

print(
    f"Accuracy: {accuracy}%"
)

print(
    f"Precision: {precision}"
)

print(
    f"Recall: {recall}"
)

print(
    f"F1 Score: {f1}"
)