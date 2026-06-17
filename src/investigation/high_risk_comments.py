import pandas as pd


def get_high_risk_comments(
    df: pd.DataFrame,
    limit: int = 10
) -> pd.DataFrame:
    #Return comments with the highest number of abuse categories.

    categories = [
        "toxic",
        "severe_toxic",
        "obscene",
        "threat",
        "insult",
        "identity_hate",
    ]

    high_risk = df.copy()

    high_risk["risk_score"] = (
        high_risk[categories]
        .sum(axis=1)
    )

    return (
        high_risk
        .sort_values(
            by="risk_score",
            ascending=False
        )
        [
            [
                "comment_text",
                "risk_score"
            ]
        ]
        .head(limit)
    )