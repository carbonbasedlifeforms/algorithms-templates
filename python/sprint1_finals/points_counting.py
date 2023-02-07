# 11 спринт, задача: Ловкость рук
# id: 81925481

from typing import Tuple

def points_counting(k: int, conc_str: str) -> int:
    numbers = set(conc_str)
    win_points = 0
    for i in numbers:
        if conc_str.count(i) <= k * 2:
            win_points += 1
    return win_points

def read_input() -> Tuple[int, str]:
    k = int(input())
    i = 0
    conc_str = ''
    for i in range(4):
        conc_str += str(input().replace('.',''))
    return k, conc_str

k, conc_str = read_input()
print(points_counting(k, conc_str))
