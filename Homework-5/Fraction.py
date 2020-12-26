class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, another_fraction):
        if self.denominator == another_fraction.denominator:
            new_numerator = self.numerator + another_fraction.numerator
            new_denominator = self.denominator
        else:
            new_numerator = self.numerator * another_fraction.denominator + another_fraction.numerator * self.denominator
            new_denominator = self.denominator * another_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, another_fraction):
        if self.denominator == another_fraction.denominator:
            new_numerator = self.numerator - another_fraction.numerator
            new_denominator = self.denominator
        else:
            new_numerator = self.numerator * another_fraction.denominator - another_fraction.numerator * self.denominator
            new_denominator = self.denominator * another_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def inverse(self):
        # mut minusul la numarator, nu il las la numitor (daca e cazul)
        if self.numerator < 0:
            return Fraction(-self.denominator, abs(self.numerator))
        return Fraction(self.denominator, self.numerator)
