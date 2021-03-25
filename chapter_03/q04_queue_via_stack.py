from typing import Optional

class LinkedListNode:
    def __init__(self, value) -> None:
        self.next: Optional[LinkedListNode] = None
        self.data = value

class Stack:
    def __init__(self) -> None:
        self.top = None

    def push(self, value):
        node = LinkedListNode(value)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        data = self.top.data
        self.top = self.top.next
        return data

    def is_empty(self):
        return self.top is None

class QueueViaStack:
    def __init__(self) -> None:
        self.stack = Stack()
        self.temp_stack = Stack()

    def add(self, value):
        while not self.stack.is_empty():
            data = self.stack.pop()
            self.temp_stack.push(data)

        self.stack.push(value)

        while not self.temp_stack.is_empty():
            data = self.temp_stack.pop()
            self.stack.push(data)

    def remove(self):
        return self.stack.pop()

queue = QueueViaStack()
queue.add(1)
queue.add(2)
queue.add(3)
assert queue.remove() == 1
assert queue.remove() == 2
queue.add(4)
assert queue.remove() == 3
assert queue.remove() == 4
