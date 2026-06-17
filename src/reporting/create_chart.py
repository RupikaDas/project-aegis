from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def create_abuse_distribution_chart(
    summary: pd.DataFrame
) -> None:

    output_dir = Path("results")

    output_dir.mkdir(
        exist_ok=True
    )

    plt.figure(figsize=(8, 5))

    plt.bar(
        summary["category"],
        summary["percent"]
    )

    plt.title(
        "Abuse Category Distribution"
    )

    plt.ylabel(
        "Percentage"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    plt.savefig(
        output_dir / "abuse_distribution.png"
    )

    plt.close()

    print(
        "Saved: results/abuse_distribution.png"
    )