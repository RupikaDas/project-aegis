# Project Aegis

> Investigating online abuse and evaluating prompt-based moderation strategies.

Project Aegis is a Trust & Safety analytics framework built to explore a simple but important question:

**Can better moderation prompts improve abuse detection while reducing moderation mistakes?**

Using the Jigsaw Toxic Comment dataset, this project analyzes large-scale user-generated content, identifies high-risk abuse patterns, benchmarks moderation prompts, and generates investigation reports that simulate real-world Trust & Safety workflows.

---

## The Problem

Every day, online platforms process millions of user-generated comments.

Trust & Safety teams must answer questions such as:

- Which comments should be reviewed first?
- What types of abuse are most common?
- How can harmful content be detected efficiently?
- How do we know if a moderation strategy is actually improving?

Project Aegis was built to explore these challenges using data analysis, risk scoring, prompt engineering, and evaluation frameworks.

---

## Key Results

### Dataset

- 159,571 comments analyzed
- 6 abuse categories
- Maximum observed risk score: 6

### Prompt Benchmarking

| Prompt | Accuracy | Precision | Recall | F1 Score |
|----------|---------:|---------:|---------:|---------:|
| V1 | 76.0% | 0.2482 | 0.7143 | 0.3684 |
| V2 | 84.6% | 0.3727 | 0.8367 | 0.5157 |
| V3 | 91.2% | 0.5294 | 0.9184 | 0.6716 |

### Outcome

Prompt V3 delivered the strongest moderation performance.

Compared to Prompt V1:

- Accuracy improved from 76.0% → 91.2%
- Recall improved from 71.4% → 91.8%
- F1 Score improved by over 82%

This demonstrates how iterative prompt refinement can significantly improve moderation quality.

---

## Project Architecture

```text
Jigsaw Toxic Comment Dataset
            |
            v
     Data Ingestion
            |
            v
      Content Analysis
            |
            v
      Risk Scoring
            |
            v
     Investigation
            |
            v
   Prompt Engineering
            |
            v
       Evaluation
            |
            v
        Reporting
            |
            v
         Results
```

---

## What Project Aegis Does

### Content Analysis

Analyzes user comments and measures the prevalence of different abuse categories.

Categories analyzed:

- Toxic
- Severe Toxic
- Obscene
- Threat
- Insult
- Identity Hate

### Risk Investigation

Identifies high-risk comments by combining multiple abuse indicators into a unified risk score.

Examples of escalated content include:

- Threats
- Hate speech
- Identity attacks
- Severe toxicity
- Multi-category abuse

### Prompt Engineering

Three moderation prompt strategies were evaluated:

- Prompt V1
- Prompt V2
- Prompt V3

Each prompt was benchmarked using the same evaluation framework to measure moderation effectiveness.

### Evaluation Framework

Performance is measured using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

This allows moderation strategies to be compared objectively.

### Reporting

Project Aegis automatically generates:

- Category summaries
- Investigation reports
- Prompt benchmark reports
- Final Trust & Safety reports
- Visualizations

---

## Abuse Distribution

| Category | Percentage |
|----------|-----------:|
| Toxic | 9.58% |
| Obscene | 5.29% |
| Insult | 4.94% |
| Severe Toxic | 1.00% |
| Identity Hate | 0.88% |
| Threat | 0.30% |

---

## Repository Structure

```text
project-aegis/
|
+-- data/
|
+-- results/
|
+-- src/
|   |
|   +-- ingestion/
|   +-- analysis/
|   +-- investigation/
|   +-- prompt_engineering/
|   +-- evaluation/
|   +-- reporting/
|
+-- docs/
|
+-- README.md
```

---

## Technology Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Git
- GitHub
- VS Code

---

## Skills Demonstrated

- Trust & Safety Analytics
- Content Moderation Analysis
- Prompt Engineering
- Risk Scoring
- Investigation Workflows
- Classification Evaluation
- Reporting Automation
- Data Analysis with Python
- Git Version Control

---

## Future Improvements

- Real LLM integration
- Human-in-the-loop moderation workflows
- Reviewer queue simulation
- Interactive moderation dashboard
- Automated moderation recommendations

---

## Why "Aegis"?

In Greek mythology, the Aegis was a shield associated with protection.

Project Aegis reflects the same idea: helping identify and investigate harmful content to support safer online communities.

---

## Author

Rupika Das

Trust & Safety Analytics | Data Analytics | Prompt Evaluation