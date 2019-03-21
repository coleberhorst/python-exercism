def largest_palindrome(max_factor, min_factor):
    if min_factor > max_factor:
        raise ValueError("Min cannot be greater than max.")
    for x in range(max_factor, min_factor - 1):
        for y in range(max_factor, min_factor):
            if str(x * y) == str(x * y)[::-1]:
                return x * y, {(x, y)}
        else:
            return None, {()}


def smallest_palindrome(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Min cannot be greater than max.")
    for x in range(min_factor, max_factor + 1):
        for y in range(min_factor, max_factor):
            if str(x * y) == str(x * y)[::-1]:
                return x * y, {(x, y)}
        else:
            return None, {()}
