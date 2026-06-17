from src.ingestion.load_data import load_csv

df = load_csv("data/raw/train.csv")

sample = df[
    [
        "comment_text",
        "toxic"
    ]
].head(20)

print(sample)