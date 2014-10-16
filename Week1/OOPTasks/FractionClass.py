from fractions import gcd


class Fraction:

    def __init__(self, a, b):
        self.nom = a
        self.denom = b

    def __add__(self, num1, num2):
        self.nom = (num2.denom * num1.nom) + (num1.denom * num2.nom)
        self.denom = abs(num1.denom * num2.denom) / gcd(num1, num2)

    def __sub__(self, num1, num2):
        self.nom = (num2.denom * num1.nom) - (num1.denom * num2.nom)
        self.denom = abs(num1.denom * num2.denom) / gcd(num1, num2)

    def __mul__(self, num1, num2):
        self.nom = num1.nom * num2.nom
        self.denom = num1.denom * num2.denom

    def __truediv__(self, num1, num2):
        self.nom = num1.nom * num2.denom
        self.denom = num1.denom * num2.nom

    def __eq__(self, num1, num2):
        if num1.nom / num1.denom == num2.nom / num2.denom:
            return True
        else:
            return False

    def __lt__(self, num1, num2):
        if num1.nom / num1.denom < num2.nom / num2.nom:
            return True
        else:
            return False

    def __gt__(self, num1, num2):
        if num1.nom / num1.denom > num2.nom / num2.nom:
            return True
        else:
            return False

    def __str__(self, num1, num2):
        


def main():
    a = Fraction(5, 4)
    b = Fraction(3, 2)


