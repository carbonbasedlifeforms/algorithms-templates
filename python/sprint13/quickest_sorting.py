# sprint 13 B.Эффективная быстрая сортировка
# ID: 83522278
from typing import List


def quicksort(contestants: list, start: int, end: int) -> List:
    if start >= end:
        return -1
    left, right = start, end
    pivot = contestants[start]

    while left <= right:
        while contestants[left] < pivot:
            left += 1
        while contestants[right] > pivot:
            right -= 1
        if left <= right:
            (contestants[left], contestants[right]) = (
                    contestants[right], contestants[left]
                )
            left += 1
            right -= 1

    quicksort(contestants, start, right)
    quicksort(contestants, left, end)


def prepare(contestants: list) -> List:
    contestants[1] = -int(contestants[1])
    contestants[2] = int(contestants[2])
    return [contestants[1], contestants[2], contestants[0]]


if __name__ == '__main__':
    qty = int(input())
    contestants = [prepare(input().split()) for item in range(qty)]
    quicksort(contestants, 0, len(contestants) - 1)
    for name in contestants:
        print(name[2])
