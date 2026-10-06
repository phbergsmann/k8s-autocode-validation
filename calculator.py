def weighted_average(values, weights):
    if not values or len(values) != len(weights):
        raise ValueError("matching nonempty inputs required")
    if any(weight < 0 for weight in weights) or sum(weights) == 0:
        raise ValueError("nonnegative weights with positive total required")
    return sum(value * weight for value, weight in zip(values, weights)) / len(values)
