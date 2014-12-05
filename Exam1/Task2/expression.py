from random import randrange
from random import choice


class Expression:

    operations = ['+', '-', '*', '//', '^']

    def __init__(self):
        self.left = randrange(1, 40)
        self.operation = choice(Expression.operations)
        self.right = randrange(1, 40)

    def __str__(self):
        return "{} {} {}".format(self.left, self.operation, self.right)

    def calculate(self):
        return eval(self.__str__())

def main():
    for i in range(1,10):
        express = Expression()
        print("{} = {}".format(express.__str__(), express.calculate()))

if __name__ == '__main__':
    main()
