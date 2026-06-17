from src.ingestion.load_data import load_csv
from src.analysis.category_summary import (
    generate_category_summary
)
from src.reporting.create_chart import (
    create_abuse_distribution_chart
)

df = load_csv("data/raw/train.csv")

summary = generate_category_summary(df)

create_abuse_distribution_chart(
    summary
)