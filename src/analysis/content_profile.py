#Content profiling module for Project Aegis.

#Provides summary statistics for Trust & Safety datasets.

import pandas as pd


def generate_content_profile(df: pd.DataFrame) -> dict:
    
    #Generate summary statistics for abuse categories.

    total_comments = len(df)

    categories = [
        "toxic",
        "severe_toxic",
        "obscene",
        "threat",
        "insult",
        "identity_hate",
    ]

    profile = {
        "total_comments": total_comments
    }

    for category in categories:
        count = int(df[category].sum())

        profile[f"{category}_count"] = count

        profile[f"{category}_percent"] = round(
            count / total_comments * 100,
            2
        )

    return profile