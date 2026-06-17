from src.evaluation.metrics import (
    calculate_accuracy
)

accuracy = calculate_accuracy(
    correct_predictions=92,
    total_predictions=100
)

print(
    f"Accuracy: {accuracy}%"
)