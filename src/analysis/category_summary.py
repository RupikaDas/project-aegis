import pandas as pd


def generate_category_summary(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Generate category-level summary statistics.
    """

    categories = [
        "toxic",
        "severe_toxic",
        "obscene",
        "threat",
        "insult",
        "identity_hate",
    ]

    summary = []

    total = len(df)

    for category in categories:

        count = int(df[category].sum())

        percent = round(
            count / total * 100,
            2
        )

        summary.append(
            {
                "category": category,
                "count": count,
                "percent": percent
            }
        )

    return pd.DataFrame(summary)