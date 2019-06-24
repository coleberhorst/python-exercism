from __future__ import division
from math import gcd


class Rational(object):
    def __init__(self, numer, denom):
        common_factor = gcd(int(numer), int(denom))
        self.numer = numer / common_factor
        if denom < 1:
            self.numer *= -1
        self.denom = abs(denom / common_factor)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + self.denom * other.numer, self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - self.denom * other.numer, self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power < 0:
            return Rational(self.denom ** abs(power), self.numer ** abs(power))
        elif power > 0:
            return Rational(self.numer ** power, self.denom ** power)
        else:
            return Rational(1, 1)

    def __rpow__(self, base):
        return (base ** self.numer) ** (1 / self.denom)
