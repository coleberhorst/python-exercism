def largest_product(series, size):
    max_product = 0
    if len(series) < size or size < 0:
        raise ValueError("Series is smaller than digit product requested.")
    for number in range(len(series)-size + 1):
        product = 1
        for i in range(size):
            product *= int(series[number + i])
        if product > max_product:
            max_product = product
    return max_product
