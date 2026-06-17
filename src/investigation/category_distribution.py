import pandas as pd


def get_category_distribution(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate abuse category distribution.
    """

    categories = [
        "toxic",
        "severe_toxic",
        "obscene",
        "threat",
        "insult",
        "identity_hate",
    ]

    results = []

    for category in categories:
        count = int(df[category].sum())

        percent = round(
            count / len(df) * 100,
            2
        )

        results.append(
            {
                "category": category,
                "count": count,
                "percent": percent,
            }
        )

    distribution = pd.DataFrame(results)

    return distribution.sort_values(
        by="percent",
        ascending=False
    )