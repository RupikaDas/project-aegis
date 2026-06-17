# Project Aegis

### AI-Assisted Trust & Safety Analytics Framework

**Author:** Rupika Das

---

## Overview

Project Aegis is a Trust & Safety analytics framework designed to investigate abusive online content, evaluate moderation strategies, benchmark prompt-engineering approaches, and generate automated investigation reports.

The project uses the Jigsaw Toxic Comment Classification dataset to simulate real-world Trust & Safety workflows commonly found in content moderation and platform integrity teams.

---

## Business Problem

Online platforms receive millions of user-generated comments every day. Moderation teams must:

* Detect abusive content
* Prioritize high-risk cases
* Reduce false positives
* Evaluate moderation quality
* Continuously improve review workflows

Project Aegis was built to demonstrate how data analytics, prompt engineering, and evaluation frameworks can support these objectives.

---

## Dataset

**Jigsaw Toxic Comment Classification Dataset**

Dataset Size:

* 159,571 comments

Categories:

* Toxic
* Severe Toxic
* Obscene
* Threat
* Insult
* Identity Hate

---

## Architecture

See:

```text
docs/architecture.md
```

Workflow:

```text
Dataset
   ↓
Data Ingestion
   ↓
Analysis
   ↓
Investigation
   ↓
Prompt Engineering
   ↓
Evaluation
   ↓
Reporting
```

---

## Key Features

### Data Ingestion

* Modular dataset loading
* Validation and logging

### Content Analysis

* Toxicity profiling
* Category distribution analysis
* Statistical summaries

### Investigation Framework

* High-risk comment detection
* Risk scoring methodology
* Abuse prioritization workflows

### Prompt Engineering

* Prompt Version 1
* Prompt Version 2
* Prompt Version 3

### Evaluation

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

### Reporting

* CSV summaries
* Benchmark reports
* Automated investigation reports
* Visual outputs

---

## Results

### Abuse Distribution

| Category      | Percentage |
| ------------- | ---------: |
| Toxic         |      9.58% |
| Obscene       |      5.29% |
| Insult        |      4.94% |
| Severe Toxic  |      1.00% |
| Identity Hate |      0.88% |
| Threat        |      0.30% |

### Prompt Benchmarking

| Prompt | Accuracy | Precision | Recall | F1 Score |
| ------ | -------: | --------: | -----: | -------: |
| V1     |    76.0% |    0.2482 | 0.7143 |   0.3684 |
| V2     |    84.6% |    0.3727 | 0.8367 |   0.5157 |
| V3     |    91.2% |    0.5294 | 0.9184 |   0.6716 |

Best Performing Prompt: **V3**

---

## Technology Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Git
* GitHub
* VS Code

---

## Skills Demonstrated

* Trust & Safety Analytics
* Data Analysis
* Prompt Engineering
* Classification Evaluation
* Risk Scoring
* Investigation Workflows
* Reporting Automation
* Python Development
* Git Version Control

---

## Future Enhancements

* LLM integration
* Real prompt evaluation
* Interactive dashboard
* Automated moderation recommendations
* Cloud deployment

---

## Author

Rupika Das
