import pandas as pd


def generate_mock_predictions(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Create mock predictions
    for evaluation testing.
    """

    sample = df[
        [
            "comment_text",
            "toxic"
        ]
    ].head(100).copy()

    sample["prediction"] = sample["toxic"]

    return sample