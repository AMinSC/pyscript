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


def lotto_number_generator(game: int):
    paper = []
    for _ in range(game):
        lotto_numbers = random.sample(range(1, 46), 6)
        paper.append(lotto_numbers)
    
    for i, v in enumerate(paper):
        paper[i] = sorted(v)
    
    return paper