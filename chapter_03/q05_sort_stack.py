from typing import Optional

class LinkedListNode:
    def __init__(self, value) -> None:
        self.next: Optional[LinkedListNode] = None
        self.data = value

class Stack:
    def __init__(self) -> None:
        self.top = None

    def __repr__(self) -> str:
        items: list = []
        node = self.top
        while node:
            items.append(node.data)
            node = node.next

        return repr(items)

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

    def peek(self):
        return self.top.data

def sort_stack(stack: Stack) -> Stack:
    temp_stack = Stack()
    while not stack.is_empty():
        tmp = stack.pop()
        while not temp_stack.is_empty() and temp_stack.peek() > tmp:
            stack.push(temp_stack.pop())
        temp_stack.push(tmp)

    # Copy elements back to the original stack with the correct ordering
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return stack

stack = Stack()
stack.push(1)
stack.push(10)
stack.push(7)
stack.push(1)
stack.push(3)
stack.push(5)
stack.push(2)
stack.push(8)
stack.push(9)
stack.push(4)
stack.push(6)

stack = sort_stack(stack)

assert stack.pop() == 1
assert stack.pop() == 1
assert stack.pop() == 2
assert stack.pop() == 3
assert stack.pop() == 4
assert stack.pop() == 5
assert stack.pop() == 6
assert stack.pop() == 7
assert stack.pop() == 8
assert stack.pop() == 9
assert stack.pop() == 10
assert stack.is_empty() is True
