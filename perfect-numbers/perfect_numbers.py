def classify(number):
    if number <= 0:
        raise ValueError("Cannot classify 0 or negative numbers.")
    aliquot = sum([x for x in range(1,number) if number % x == 0 and x != number])
    return (aliquot < number) * "deficient" + (aliquot == number) * "perfect" + (aliquot > number) * "abundant"
