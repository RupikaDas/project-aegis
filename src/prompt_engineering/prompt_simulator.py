import pandas as pd
import random


def simulate_prompt_v1(
    df: pd.DataFrame
) -> pd.DataFrame:

    sample = df[
        [
            "comment_text",
            "toxic"
        ]
    ].head(500).copy()

    predictions = []

    for actual in sample["toxic"]:

        if random.random() < 0.75:
            predictions.append(actual)

        else:
            predictions.append(
                1 - actual
            )

    sample["prediction"] = predictions

    return sample

def simulate_prompt_v2(
    df: pd.DataFrame
) -> pd.DataFrame:

    sample = df[
        [
            "comment_text",
            "toxic"
        ]
    ].head(500).copy()

    predictions = []

    for actual in sample["toxic"]:

        if random.random() < 0.85:
            predictions.append(actual)

        else:
            predictions.append(
                1 - actual
            )

    sample["prediction"] = predictions

    return sample

def simulate_prompt_v3(
    df: pd.DataFrame
) -> pd.DataFrame:

    sample = df[
        [
            "comment_text",
            "toxic"
        ]
    ].head(500).copy()

    predictions = []

    for actual in sample["toxic"]:

        if random.random() < 0.92:
            predictions.append(actual)

        else:
            predictions.append(
                1 - actual
            )

    sample["prediction"] = predictions

    return sample