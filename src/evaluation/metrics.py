def calculate_accuracy(
    actual: list,
    predicted: list
) -> float:
    """
    Calculate classification accuracy.
    """

    if len(actual) != len(predicted):
        raise ValueError(
            "Lists must have same length."
        )

    correct = sum(
        a == p
        for a, p in zip(actual, predicted)
    )

    return round(
        correct / len(actual) * 100,
        2
    )