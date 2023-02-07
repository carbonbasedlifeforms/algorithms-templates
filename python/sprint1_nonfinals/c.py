from typing import List, Tuple

def get_neighbours(matrix: List[List[int]], row: int, col: int, row_limit: int, col_limit: int) -> List[int]:
    result = []
    for i in (-1, 1):
        if  0 <= row + i <= n-1 and row_limit > 1:
            result.append(matrix[row+i][col])
        if 0 <= col + i <= col_limit-1 and col_limit > 1:
            result.append(matrix[row][col + i])
    result.sort()
    return result

def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col, n, m

matrix, row, col, n, m = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col, n, m))))
