from typing import Optional


class LinkedListNode:
    def __init__(self, value) -> None:
        self.data = value
        self.next: Optional[LinkedListNode] = None
        self.next_min_node: Optional[LinkedListNode] = None


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.node_min_value = None

    def push(self, value):
        node = LinkedListNode(value)
        if self.top:
            node.next = self.top
        self.top = node

        # First pushed item
        if self.node_min_value is None:
            self.node_min_value = self.top

        # If the new pushed value is lower, update the references
        if value <= self.node_min_value.data:
            self.top.next_min_node = self.node_min_value
            self.node_min_value = self.top

    def pop(self):
        if not self.top:
            raise RuntimeError("Empty stack")

        # Update reference to the new lowest value
        if self.top is self.node_min_value:
            self.node_min_value = self.node_min_value.next_min_node

        data = self.top.data
        self.top = self.top.next

        if self.top is None:
            self.node_min_value = None

        return data

    def min(self):
        if self.node_min_value is None:
            raise RuntimeError("Empty stack")

        return self.node_min_value.data

stack = Stack()

stack.push(2)
assert stack.min() == 2
stack.push(3)
assert stack.min() == 2
stack.push(1)
assert stack.min() == 1

assert stack.pop() == 1
assert stack.min() == 2
assert stack.pop() == 3
assert stack.min() == 2
assert stack.pop() == 2

stack.push(5)
assert stack.min() == 5
stack.push(6)
assert stack.min() == 5
stack.push(3)
assert stack.min() == 3
stack.push(7)
assert stack.min() == 3

assert stack.pop() == 7
assert stack.min() == 3
assert stack.pop() == 3
assert stack.min() == 5
