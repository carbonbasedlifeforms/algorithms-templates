# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node):
    # Your code
    # ヽ(´▽`)/
    while node:
        print(node.value)
        node = node.next_item
