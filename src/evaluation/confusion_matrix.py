import pandas as pd


def create_confusion_matrix(
    df: pd.DataFrame
) -> dict:

    tp = len(
        df[
            (df["toxic"] == 1)
            &
            (df["prediction"] == 1)
        ]
    )

    tn = len(
        df[
            (df["toxic"] == 0)
            &
            (df["prediction"] == 0)
        ]
    )

    fp = len(
        df[
            (df["toxic"] == 0)
            &
            (df["prediction"] == 1)
        ]
    )

    fn = len(
        df[
            (df["toxic"] == 1)
            &
            (df["prediction"] == 0)
        ]
    )

    return {
        "True Positive": tp,
        "True Negative": tn,
        "False Positive": fp,
        "False Negative": fn
    }