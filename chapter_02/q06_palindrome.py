from linked_list import LinkedList, LinkedListNode

class Stack:
    def __init__(self) -> None:
        self.linked_list = LinkedList([])
        self.top = self.linked_list.head

    def push(self, item):
        new_node = LinkedListNode(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        data = self.top.data
        self.top = self.top.next
        return data

def is_palindrome(linked_list: LinkedList) -> bool:
    stack = Stack()
    node = linked_list.head
    while node:
        stack.push(node.data)
        node = node.next

    node = linked_list.head
    while node:
        data = stack.pop()
        if data != node.data:
            return False
        node = node.next

    return True

assert is_palindrome(LinkedList([1,2,3,2,1])) is True
assert is_palindrome(LinkedList([1,2,2,1])) is True
assert is_palindrome(LinkedList([0,1,2,2,1])) is False
assert is_palindrome(LinkedList([1,2,3,2,1,1])) is False
