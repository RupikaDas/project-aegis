from src.ingestion.load_data import load_csv
from src.prompt_engineering.prompt_versions import (
    prompt_v1,
    prompt_v2,
    prompt_v3,
)

df = load_csv("data/raw/train.csv")

comment = df.iloc[0]["comment_text"]

print("===== PROMPT V1 =====")
print(prompt_v1(comment))

print("\n===== PROMPT V2 =====")
print(prompt_v2(comment))

print("\n===== PROMPT V3 =====")
print(prompt_v3(comment))