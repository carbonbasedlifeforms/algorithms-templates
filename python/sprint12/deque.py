# 12 sprint, Дек
# id: 82895673
from typing import List


class Deque:
    def __init__(self, deque_mx_len: int) -> None:
        self.cells: List[int] = [None] * deque_mx_len
        self.max_length: int = deque_mx_len
        self.head_idx: int = -1
        self.tail_idx: int = 0
        self.size: int = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def is_filled(self) -> bool:
        return self.size == self.max_length

    def calc_idx(self, idx: int, increment: int) -> int:
        return (idx + increment) % self.max_length

    def push_front(self, value: int) -> None:
        if self.is_filled():
            raise IndexError('error')
        self.cells[self.head_idx] = value
        self.head_idx = self.calc_idx(self.head_idx, -1)
        self.size += 1

    def push_back(self, value: int) -> None:
        if self.is_filled():
            raise IndexError('error')
        self.cells[self.tail_idx] = value
        self.tail_idx = self.calc_idx(self.tail_idx, 1)
        self.size += 1

    def pop_front(self) -> int:
        if self.is_empty():
            raise IOError('error')
        self.head_idx = self.calc_idx(self.head_idx, 1)
        pop_value = self.cells[self.head_idx]
        self.cells[self.head_idx] = None
        self.size -= 1
        return pop_value

    def pop_back(self) -> int:
        if self.is_empty():
            raise IOError('error')
        self.tail_idx = self.calc_idx(self.tail_idx, -1)
        pop_value = self.cells[self.tail_idx]
        self.cells[self.tail_idx] = None
        self.size -= 1
        return pop_value


if __name__ == '__main__':
    cmd_qty = int(input())
    deque_mx_len = int(input())
    deque = Deque(deque_mx_len)
    for cmd in range(cmd_qty):
        cmd, *param = input().split()
        try:
            func = getattr(deque, cmd)
            answer = func(*param)
            if answer:
                print(answer)
        except (IndexError, IOError):
            print('error')
