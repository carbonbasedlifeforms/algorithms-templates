# 11 спринт, задача: Ближайший ноль
# id: 81919290

from typing import List, Tuple

def nearest_zero(elements_qty: int, input_struct: List[int]) -> List[int]:
    result = [0] * elements_qty
    zero_idx = []

    for idx, value in enumerate(input_struct):
        if value == 0:
            zero_idx.append(idx)

    for i in range(zero_idx[0]):
        result[i] = zero_idx[0] - i

    for i in range(zero_idx[-1] + 1, elements_qty):
        result[i] = i - zero_idx[-1]

    for n in range(len(zero_idx)-1):
        for i in range(zero_idx[n] + 1, zero_idx[n + 1]):
            result[i] = min(i - zero_idx[n], zero_idx[n + 1] - i)
    return result

def read_input() -> Tuple[int, List[int]]:
    elements_qty = int(input())
    input_struct = list(map(int, input().strip().split()))
    return elements_qty, input_struct

elements_qty, input_struct = read_input()
print(" ".join(map(str, nearest_zero(elements_qty, input_struct))))
