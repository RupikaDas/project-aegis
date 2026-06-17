from src.ingestion.load_data import load_csv
from src.analysis.category_summary import (
    generate_category_summary
)

df = load_csv("data/raw/train.csv")

summary = generate_category_summary(df)

print(summary)