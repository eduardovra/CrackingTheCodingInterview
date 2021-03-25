from typing import Optional

class LinkedListNode:
    def __init__(self, value) -> None:
        self.previous: Optional[LinkedListNode] = None
        self.next: Optional[LinkedListNode] = None
        self.data = value

class Stack:
    STACK_LENGTH = 3

    def __init__(self) -> None:
        self.top = None
        self.items = 0

    def push(self, value):
        node = LinkedListNode(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.items += 1

    def pop(self):
        data = self.top.data
        self.top = self.top.next
        self.items -= 1
        return data

    def is_full(self):
        return self.items == self.STACK_LENGTH

    def is_empty(self):
        return self.items == 0

class SetOfStacks:
    def __init__(self) -> None:
        new_stack = Stack()
        # Add new stack to the stacks list
        self.stacks_list = LinkedListNode(new_stack)
        # Update current active stack reference
        self.current_stack = self.stacks_list

    def push(self, value):
        stack = self.current_stack.data
        # If current stack is full, create a new stack
        if stack.is_full():
            stack = self.add_stack()
        # Push the value on top of the stack
        stack.push(value)

    def pop(self):
        stack = self.current_stack.data
        # Pop element
        value = stack.pop()
        # If the stack is empty remove it from the linked_list of stacks and update the current stack index
        if stack.is_empty():
            self.drop_stack()
        # Return the value
        return value

    def popAt(self, index):
        # Traverse the list of stacks until the desired index is reached
        node = self.get_stack(index)
        # If the stack doesn't exists, raise an exception
        # If the stack is empty, raise an exception
        # Pop element
        stack = node.data
        value = stack.pop()
        # If the stack becomes empty, drop it
        if stack.is_empty():
            self.drop_stack(index)

        return value

    def add_stack(self):
        new_stack = Stack()
        node = LinkedListNode(new_stack)
        node.previous = self.current_stack
        self.current_stack.next = node
        self.current_stack = node
        return self.current_stack.data

    def drop_stack(self, index = None):
        # If index is None, drop the current stack
        if index is None:
            stack_to_drop = self.current_stack
        else:
            stack_to_drop = self.get_stack(index)

        self.current_stack = stack_to_drop.previous

        if stack_to_drop.previous:
            stack_to_drop.previous.next = stack_to_drop.next

        if stack_to_drop.next:
            stack_to_drop.next.previous = stack_to_drop.previous

    def get_stack(self, index):
        node = self.stacks_list
        while index:
            index -= 1
            node = node.next
        return node

stack = SetOfStacks()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)

assert stack.pop() == 6
assert stack.popAt(0) == 3
assert stack.popAt(1) == 5
assert stack.pop() == 4
assert stack.popAt(0) == 2
assert stack.pop() == 1
