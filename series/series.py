def slices(series, length):
    if length > len(series) or length <= 0:
        raise ValueError("Length of subseries cannot be greater than series.")
    return [series[i:i+length] for i in range(len(series) - length + 1)]
