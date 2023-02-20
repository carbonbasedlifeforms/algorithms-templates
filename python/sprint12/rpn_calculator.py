# 12 sprint, Калькулятор
# id: 82657057
from operator import add, floordiv, mul, sub


OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': floordiv
}


class Calculation:
    def __init__(self):
        self.result = []

    def is_number(self, element: str) -> bool:
        try:
            float(element)
            return True
        except ValueError:
            return False

    def push(self, value):
        self.result.append(value)

    def pop(self):
        try:
            return self.result.pop()
        except IndexError:
            return


def rpn_calculator():
    expr = input().split()
    characters = Calculation()

    for element in expr:
        if characters.is_number(element):
            characters.push(int(element))
        else:
            operand1, operand2 = characters.pop(), characters.pop()
            atom_calc = OPERATORS[element](operand2, operand1)
            characters.push(atom_calc)

    print(characters.pop())


if __name__ == '__main__':
    rpn_calculator()
