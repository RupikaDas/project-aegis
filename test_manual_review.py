from src.ingestion.load_data import load_csv
from src.evaluation.manual_review import (
    create_review_set
)

df = load_csv("data/raw/train.csv")

review_set = create_review_set(df)

print(review_set)