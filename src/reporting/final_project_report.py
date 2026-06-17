from pathlib import Path


def create_final_project_report():

    report = """
PROJECT AEGIS
Trust & Safety Analytics Framework

========================================
DATASET OVERVIEW
========================================

Total Comments: 159571

Toxic: 15294 (9.58%)
Severe Toxic: 1595 (1.00%)
Obscene: 8449 (5.29%)
Threat: 478 (0.30%)
Insult: 7877 (4.94%)
Identity Hate: 1405 (0.88%)

========================================
HIGH RISK INVESTIGATION
========================================

Identified comments containing multiple
abuse categories simultaneously.

Maximum Risk Score Observed: 6

High-risk comments included:
- Threats
- Hate speech
- Identity attacks
- Obscene language
- Severe toxicity

========================================
PROMPT EVALUATION
========================================

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

Best Performing Prompt: V3

========================================
TRUST & SAFETY RECOMMENDATIONS
========================================

1. Prioritize review of comments with
   risk score >= 4.

2. Use Prompt V3 for first-pass
   moderation.

3. Escalate comments containing
   threat or identity_hate labels.

4. Continue prompt refinement to
   improve precision and reduce
   false positives.

========================================
END OF REPORT
========================================
"""

    output_dir = Path("results")

    output_dir.mkdir(
        exist_ok=True
    )

    with open(
        output_dir / "final_project_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)

    print(
        "Saved: results/final_project_report.txt"
    )