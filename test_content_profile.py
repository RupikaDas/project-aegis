from src.ingestion.load_data import load_csv
from src.analysis.content_profile import generate_content_profile

df = load_csv("data/raw/train.csv")

profile = generate_content_profile(df)

print("\n=== CONTENT PROFILE ===\n")

for key, value in profile.items():
    print(f"{key}: {value}")