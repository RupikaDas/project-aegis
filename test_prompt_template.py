from src.ingestion.load_data import load_csv
from src.prompt_engineering.prompt_templates import (
    toxicity_classification_prompt
)

df = load_csv("data/raw/train.csv")

comment = df.iloc[0]["comment_text"]

prompt = toxicity_classification_prompt(comment)

print(prompt)