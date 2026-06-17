from src.ingestion.load_data import load_csv
from src.evaluation.mock_predictions import (
    generate_mock_predictions
)

df = load_csv("data/raw/train.csv")

predictions = generate_mock_predictions(df)

print(
    predictions.head()
)