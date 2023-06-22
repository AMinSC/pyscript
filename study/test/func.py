import random


class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed"
        else:
            return a / b


def random_add(num):
    return num + random.randint(1, 10)
