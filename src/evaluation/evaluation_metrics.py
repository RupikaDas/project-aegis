import pandas as pd


def calculate_accuracy(df: pd.DataFrame) -> float:

    correct = (
        df["toxic"] == df["prediction"]
    ).sum()

    total = len(df)

    return round(
        (correct / total) * 100,
        2
    )


def calculate_precision(
    df: pd.DataFrame
) -> float:

    true_positive = len(
        df[
            (df["toxic"] == 1)
            &
            (df["prediction"] == 1)
        ]
    )

    predicted_positive = len(
        df[
            df["prediction"] == 1
        ]
    )

    if predicted_positive == 0:
        return 0.0

    return round(
        true_positive / predicted_positive,
        4
    )


def calculate_recall(
    df: pd.DataFrame
) -> float:

    true_positive = len(
        df[
            (df["toxic"] == 1)
            &
            (df["prediction"] == 1)
        ]
    )

    actual_positive = len(
        df[
            df["toxic"] == 1
        ]
    )

    if actual_positive == 0:
        return 0.0

    return round(
        true_positive / actual_positive,
        4
    )


def calculate_f1(
    precision: float,
    recall: float
) -> float:

    if precision + recall == 0:
        return 0.0

    return round(
        (
            2 * precision * recall
        )
        /
        (
            precision + recall
        ),
        4
    )