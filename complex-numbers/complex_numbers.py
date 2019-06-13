from math import sqrt


class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __abs__(self):
        return sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        pass

    def exp(self):
        pass
