# 11 спринт, задача: Ближайший ноль
# id: 81971250

from typing import List, Tuple

def nearest_zero(elements_qty: int, input_struct: List[int]) -> List[int]:
    distances = [0] * elements_qty
    empty_sites = []

    for idx, value in enumerate(input_struct):
        if value == 0:
            empty_sites.append(idx)

    for idx in range(empty_sites[0]):
        distances[idx] = empty_sites[0] - idx

    for idx in range(empty_sites[-1] + 1, elements_qty):
        distances[idx] = idx - empty_sites[-1]

    for znum in range(len(empty_sites)-1):
        for idx in range(empty_sites[znum] + 1, empty_sites[znum + 1]):
            distances[idx] = min(idx - empty_sites[znum], empty_sites[znum + 1] - idx)
    return distances

def read_input() -> Tuple[int, List[int]]:
    elements_qty = int(input())
    input_struct = list(map(int, input().strip().split()))
    return elements_qty, input_struct

elements_qty, input_struct = read_input()
print(" ".join(map(str, nearest_zero(elements_qty, input_struct))))
