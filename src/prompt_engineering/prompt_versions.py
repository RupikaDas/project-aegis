def prompt_v1(comment: str) -> str:
    return f"""
Classify this comment as Toxic or Safe.

Comment:
{comment}
"""


def prompt_v2(comment: str) -> str:
    return f"""
Classify the comment into:
- Toxic
- Threat
- Insult
- Identity Hate
- Safe

Comment:
{comment}

Return your reasoning.
"""


def prompt_v3(comment: str) -> str:
    return f"""
You are an expert YouTube Trust & Safety analyst.

Analyze the comment and determine whether it contains:

- Toxicity
- Severe Toxicity
- Obscene Language
- Threats
- Insults
- Identity Hate

For each category provide:

1. Yes/No
2. Confidence Score (0-100)
3. Explanation

Comment:
{comment}

Return valid JSON only.
"""