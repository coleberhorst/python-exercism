def collatz_steps(number):
    if number <= 0:
        raise ValueError("Collatz steps cannot be caluclated for numbers below 1.")
    steps = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = 3 * number + 1
        steps += 1
    return steps
