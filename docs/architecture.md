# Project Aegis Architecture

Jigsaw Toxic Comment Dataset
            |
            v
+----------------------+
|   Data Ingestion     |
|  load_data.py        |
+----------------------+
            |
            v
+----------------------+
|      Analysis        |
| content_profile.py   |
| category_summary.py  |
+----------------------+
            |
            v
+----------------------+
|   Investigation      |
| high_risk_comments   |
| category_distribution|
+----------------------+
            |
            v
+----------------------+
| Prompt Engineering   |
| Prompt V1            |
| Prompt V2            |
| Prompt V3            |
+----------------------+
            |
            v
+----------------------+
|     Evaluation       |
| Accuracy             |
| Precision            |
| Recall               |
| F1 Score             |
| Confusion Matrix     |
+----------------------+
            |
            v
+----------------------+
|      Reporting       |
| CSV Outputs          |
| Visualizations       |
| Benchmark Reports    |
| Final Report         |
+----------------------+
            |
            v
+----------------------+
|      Results         |
| PNG Charts           |
| TXT Reports          |
| CSV Summaries        |
+----------------------+