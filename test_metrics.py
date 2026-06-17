from src.evaluation.metrics import (
    calculate_accuracy
)

actual = [
    "toxic",
    "safe",
    "toxic",
    "safe",
    "toxic"
]

predicted = [
    "toxic",
    "safe",
    "safe",
    "safe",
    "toxic"
]

accuracy = calculate_accuracy(
    actual,
    predicted
)

print(
    f"Accuracy: {accuracy}%"
)