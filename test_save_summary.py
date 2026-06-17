from src.ingestion.load_data import load_csv
from src.analysis.category_summary import (
    generate_category_summary
)
from src.reporting.save_summary import (
    save_category_summary
)

df = load_csv("data/raw/train.csv")

summary = generate_category_summary(df)

save_category_summary(summary)