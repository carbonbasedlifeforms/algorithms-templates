# 12 sprint, Калькулятор
# id: 82764129
from operator import add, floordiv, mul, sub
from typing import List, Dict


class Stack:
    def __init__(self):
        self.result = []

    def push(self, value: str):
        self.result.append(value)

    def pop(self):
        if not self.result:
            exit(0)
        return self.result.pop()


def rpn_calculator(expr: List[str], operators: Dict[str, str]) -> int:
    characters = Stack()
    for element in expr:
        if element in operators:
            operand1, operand2 = characters.pop(), characters.pop()
            atom_calc = operators[element](operand2, operand1)
            characters.push(atom_calc)
        else:
            characters.push(int(element))
    print(characters.pop())


if __name__ == '__main__':

    OPERATORS = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': floordiv
    }
    expr = input().split()
    rpn_calculator(expr, OPERATORS)
