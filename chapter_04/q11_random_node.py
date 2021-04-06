from typing import Optional
from random import randrange

class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __repr__(self) -> str:
        return str(self.data)

class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        self.length = 0

    def insert(self, value, node):
        if not node:
            # First insertion
            self.root = Node(value)
            self.length = 1
            return self.root
        elif value <= node.data:
            # If value is less than current node, insert on left side
            if node.left:
                self.insert(value, node.left)
            else:
                node.left = Node(value)
                self.length += 1
                return node.left
        else:
            # If value is greater than current node, insert on right side
            if node.right:
                self.insert(value, node.right)
            else:
                node.right = Node(value)
                self.length += 1
                return node.right

    def _find_recursive(self, node, value):
        if node.left:
            n = self._find_recursive(node.left, value)
            if n:
                return n
        if node.data == value:
            return node
        if node.right:
            n = self._find_recursive(node.right, value)
            if n:
                return n

        return None

    def find(self, value):
        return self._find_recursive(self.root, value)

    def delete(self, value):
        node = self.find(value)
        # TODO

    def _get_node_depth(self, node, depth):
        if depth == 0:
            return node
        if node.left:
            n = self._get_node_depth(node.left, depth - 1)
            if n:
                return n
        if node.right:
            n = self._get_node_depth(node.right, depth - 1)
            if n:
                return n

        return None

    def get_random_node(self):
        rand_depth = randrange(self.length)
        return self._get_node_depth(self.root, rand_depth)

bt = BinaryTree()
n8 = bt.insert(8, None)
n4 = bt.insert(4, n8)
n2 = bt.insert(2, n4)
n6 = bt.insert(6, n4)
n10 = bt.insert(10, n8)
n20 = bt.insert(20, n10)

node = bt.get_random_node()

assert bt.length == 6

assert bt.find(6) is n6

bt.delete(6)

assert bt.find(6) is None
