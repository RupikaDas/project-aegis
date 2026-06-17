from pathlib import Path
import pandas as pd


def save_category_summary(
    summary: pd.DataFrame
) -> None:
    #Save category summary to CSV.

    output_dir = Path("results")

    output_dir.mkdir(
        exist_ok=True
    )

    summary.to_csv(
        output_dir / "category_summary.csv",
        index=False
    )

    print(
        "Saved: results/category_summary.csv"
    )