def is_equilateral(sides):
    return len(set(sides)) == 1 and is_triangle(sides)


def is_isosceles(sides):
    return len(set(sides)) < 3 and is_triangle(sides)


def is_scalene(sides):
    return len(set(sides)) == 3 and is_triangle(sides)


def is_triangle(sides):
    return all(sides) and 2*max(sides) < sum(sides)
