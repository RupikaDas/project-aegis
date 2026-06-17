import pandas as pd


def create_review_set(
    df: pd.DataFrame,
    size: int = 20
) -> pd.DataFrame:
    """
    Create a sample set for manual review.
    """

    return df[
        [
            "comment_text",
            "toxic"
        ]
    ].sample(
        n=size,
        random_state=42
    )