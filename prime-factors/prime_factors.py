def prime_factors(natural_number):
    factors, n = [], 2
    while natural_number > 1:
        while natural_number % n == 0:
            factors.append(n)
            natural_number /= n
        n += 1
    return factors
