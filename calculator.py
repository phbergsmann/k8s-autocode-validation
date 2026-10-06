def weighted_average(values, weights):
    """Return the weighted average of *values*.

    Raises:
        ValueError: if the inputs are empty or mismatched in length, if any
            weight is negative, or if the total weight is zero.
    """
    if not values or len(values) != len(weights):
        raise ValueError("matching nonempty inputs required")
    if any(weight < 0 for weight in weights) or sum(weights) == 0:
        raise ValueError("nonnegative weights with positive total required")
    return sum(value * weight for value, weight in zip(values, weights)) / sum(weights)
