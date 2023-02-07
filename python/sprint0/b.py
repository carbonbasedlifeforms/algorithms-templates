from typing import List, Tuple

def zipper(a: List[int], b: List[int], n: int) -> List[int]:
    c = []
    for i in range(n):
        c.append(a[i])
        c.append(b[i])
    return c

def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b, n

a, b, n = read_input()
print(" ".join(map(str, zipper(a, b, n))))
