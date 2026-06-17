from src.ingestion.load_data import load_csv

from src.evaluation.mock_predictions import (
    generate_mock_predictions
)

from src.evaluation.confusion_matrix import (
    create_confusion_matrix
)

df = load_csv(
    "data/raw/train.csv"
)

predictions = generate_mock_predictions(df)

matrix = create_confusion_matrix(
    predictions
)

print()

for key, value in matrix.items():
    print(
        f"{key}: {value}"
    )