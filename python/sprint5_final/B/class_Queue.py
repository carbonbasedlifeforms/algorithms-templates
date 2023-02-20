from typing import List


class Queue:
    def __init__(self, mx_len: int):
        self.queue: List[int] = [None] * mx_len
        self.max_length: int = mx_len
        self.head: int = 0
        self.tail: int = 0
        self.size: int = 0

    def is_empty(self) -> int:
        return self.size == 0

    def push(self, value: int) -> None:
        if self.size != self.max_length:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_length
            self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_length
        self.size -= 1
        return x


q = Queue(8)
q.push(1)
print(q.queue)  # [1, None, None, None, None, None, None, None]
print(q.size)   # 1
q.push(-1)
q.push(0)
q.push(11)
print(q.queue)  # [1, -1, 0, 11, None, None, None, None]
print(q.size)   # 4

print(q.head)
q.pop()
print(q.queue)
q.pop()
print(q.queue)
print(q.head)
