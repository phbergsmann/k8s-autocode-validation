def weighted_average(values, weights):
    """Return the weighted average of ``values`` using ``weights``.

    Args:
        values: Sequence of numeric values to average.
        weights: Sequence of nonnegative weights, same length as ``values``.

    Returns:
        The sum of value*weight divided by the sum of weights.

    Raises:
        ValueError: If ``values`` is empty or ``len(values) != len(weights)``
            (message: "matching nonempty inputs required"), or if any weight
            is negative or the sum of weights is zero (message:
            "nonnegative weights with positive total required").
    """
    if not values or len(values) != len(weights):
        raise ValueError("matching nonempty inputs required")
    if any(weight < 0 for weight in weights) or sum(weights) == 0:
        raise ValueError("nonnegative weights with positive total required")
    return sum(value * weight for value, weight in zip(values, weights)) / sum(weights)
