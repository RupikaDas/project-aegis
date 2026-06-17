def toxicity_classification_prompt(
    comment: str
) -> str:
    """
    Generate a Trust & Safety classification prompt.
    """

    return f"""

Analyze the following comment.

Classify it into one or more categories:

- Toxic
- Severe Toxic
- Obscene
- Threat
- Insult
- Identity Hate
- Safe

For each category provide:
1. Yes or No
2. Confidence score (0-100)

Comment:
{comment}

Return the result as structured JSON.
"""