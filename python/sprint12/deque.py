# 12 sprint, Дек
# id: 82656997
from typing import List


class Deque:
    def __init__(self, deque_mx_len: int) -> None:
        self.deque: List[int] = [None] * deque_mx_len
        self.max_length: int = deque_mx_len
        self.head_idx: int = 0
        self.tail_idx: int = 0
        self.size: int = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def zeroing_indexes(self) -> None:
        if self.is_empty():
            self.head_idx = 0
            self.tail_idx = 0

    def is_filled(self) -> bool:
        return self.size == self.max_length

    def push_front(self, value: int) -> None:
        if self.is_filled():
            raise IndexError('error')
        if self.is_empty():
            self.tail_idx += 1
        self.deque[self.head_idx] = value
        self.head_idx = (self.head_idx - 1) % self.max_length
        self.size += 1

    def push_back(self, value: int) -> None:
        if self.is_filled():
            raise IndexError('error')
        if self.is_empty():
            self.head_idx = self.max_length - 1
        self.deque[self.tail_idx] = value
        self.tail_idx = (self.tail_idx + 1) % self.max_length
        self.size += 1

    def pop_front(self) -> int:
        if self.is_empty():
            raise IOError('error')
        self.head_idx = (self.head_idx + 1) % self.max_length
        pop_value = self.deque[self.head_idx]
        self.deque[self.head_idx] = None
        self.size -= 1
        self.zeroing_indexes()
        return pop_value

    def pop_back(self) -> int:
        if self.is_empty():
            raise IOError('error')
        self.tail_idx = (self.tail_idx - 1) % self.max_length
        pop_value = self.deque[self.tail_idx]
        self.deque[self.tail_idx] = None
        self.size -= 1
        self.zeroing_indexes()
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
