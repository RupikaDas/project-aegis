def calculate_accuracy(
    correct_predictions: int,
    total_predictions: int
) -> float:
    """
    Calculate classification accuracy.
    """

    if total_predictions == 0:
        return 0.0

    return round(
        correct_predictions / total_predictions * 100,
        2
    )