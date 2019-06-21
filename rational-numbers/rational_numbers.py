from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        self.simplify()

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def simplify(self):
        a, b = self.numer, self.denom
        while b:
            a, b = b, a % b
        self.numer, self.denom = self.numer / a, self.denom / a
        if not self.numer:
            self.denom = 1
        if not self.denom:
            raise ZeroDivisionError()

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        self.numer, self.denom = self.numer * other.denom + self.denom * other.numer, self.denom * other.denom
        self.simplify()
        return self

    def __sub__(self, other):
        self.numer, self.denom = self.numer * other.denom - self.denom * other.numer, self.denom * other.denom
        self.simplify()
        return self

    def __mul__(self, other):
        print(self, other)
        self.numer, self.denom = self.numer * self.denom, other.numer * other.denom
        self.simplify()
        print(self)
        return self

    def __truediv__(self, other):
        self.numer = self.numer * other.denom
        self.denom = self.denom * other.numer
        self.simplify()
        return self

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        pass

    def __rpow__(self, base):
        pass
