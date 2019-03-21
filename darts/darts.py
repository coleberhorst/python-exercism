from math import sqrt


def score(x, y):
    radius = sqrt(x**2 + y**2)
    if radius > 10:
        return 0
    elif radius > 5:
        return 1
    elif radius > 1:
        return 5
    elif radius > 0:
        return 10
        
