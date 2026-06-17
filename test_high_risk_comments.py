from src.ingestion.load_data import load_csv
from src.investigation.high_risk_comments import (
    get_high_risk_comments
)

df = load_csv("data/raw/train.csv")

results = get_high_risk_comments(df)

print(results)