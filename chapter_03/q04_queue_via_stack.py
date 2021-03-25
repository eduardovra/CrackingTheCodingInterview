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
        self.add_stack = Stack()
        self.rem_stack = Stack()

    def add(self, value):
        while not self.rem_stack.is_empty():
            data = self.rem_stack.pop()
            self.add_stack.push(data)
        self.add_stack.push(value)

    def remove(self):
        while not self.add_stack.is_empty():
            data = self.add_stack.pop()
            if self.add_stack.is_empty():
                return data # Last element
            self.rem_stack.push(data)

        return self.rem_stack.pop()

queue = QueueViaStack()
queue.add(1)
queue.add(2)
queue.add(3)
queue.add(4)
assert queue.remove() == 1
assert queue.remove() == 2
queue.add(5)
queue.add(6)
assert queue.remove() == 3
queue.add(7)
assert queue.remove() == 4
assert queue.remove() == 5
assert queue.remove() == 6
assert queue.remove() == 7
