result = []

row = 3
col = 0

row_limit = 8
col_limit = 9

matrix = [
[3, 3, -9, 7, -5, 8, -6, -10, -4],
[5, -2, -6, -9, 8, -4, 5, -5, 0],
[-9, -3, 3, 2, 1, -4, -6, 3, -9],
[-7, 1, -2, 4, -2, 1, -5, 4, -8],
[-2, 5, 5, 7, -7, 2, 3, -4, -4],
[-1, 7, -10, 7, 4, 5, -7, 1, 5],
[-1, 3, 0, -8, -10, -2, 5, 1, 7],
[10, 4, -9, 5, 3, -1, 7, 10, -5]
]
for i in (-1, 1):
    if  0 <= row + i <= row_limit-1 and row_limit > 1:
        result.append(matrix[row+i][col])
        # print(neighbour_row)
        # if neighbour_row not in result:
        #     result.append(neighbour_row)
    if 0 <= col + i <= col_limit-1 and col_limit > 1:
        result.append(matrix[row][col + i])
        # if neighbour_col not in result:
        #     result.append(neighbour_col)

result.sort()

print(result)
    



# result = set()

# a = 6
# b = 6
# c = 2
# d = 1
# f = 2

# result.add(a)
# result.add(b)
# result.add(c)
# result.add(d)
# result.add(f)

# print(result)
# print(list(result))
