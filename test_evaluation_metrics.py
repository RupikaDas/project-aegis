from src.ingestion.load_data import load_csv

from src.evaluation.mock_predictions import (
    generate_mock_predictions
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

predictions = generate_mock_predictions(df)

accuracy = calculate_accuracy(
    predictions
)

precision = calculate_precision(
    predictions
)

recall = calculate_recall(
    predictions
)

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