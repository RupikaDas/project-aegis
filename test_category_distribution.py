from src.ingestion.load_data import load_csv
from src.investigation.category_distribution import (
    get_category_distribution,
)

df = load_csv("data/raw/train.csv")

distribution = get_category_distribution(df)

print(distribution)