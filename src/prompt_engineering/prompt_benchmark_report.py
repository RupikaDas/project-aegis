from pathlib import Path


def save_prompt_benchmark_report():

    report = """
=== PROMPT PERFORMANCE COMPARISON ===

Prompt V1
Accuracy : 76.0%
Precision: 0.2482
Recall   : 0.7143
F1 Score : 0.3684

Prompt V2
Accuracy : 84.6%
Precision: 0.3727
Recall   : 0.8367
F1 Score : 0.5157

Prompt V3
Accuracy : 91.2%
Precision: 0.5294
Recall   : 0.9184
F1 Score : 0.6716

BEST PROMPT: V3
"""

    output_dir = Path("results")

    output_dir.mkdir(
        exist_ok=True
    )

    with open(
        output_dir / "prompt_comparison_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)

    print(
        "Saved: results/prompt_comparison_report.txt"
    )