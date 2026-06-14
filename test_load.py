from src.ingestion.load_data import load_csv

df = load_csv("data/raw/train.csv")

print(df.head())
print(df.shape)