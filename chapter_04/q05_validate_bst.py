from typing import Optional

class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
    
    def __repr__(self) -> str:
        return f"Data: {self.data} Left: {repr(self.left)} Right: {repr(self.right)}"

def check_bst(node: Optional[Node], min_value, max_value):
    if not node:
        return True

    print(f"Data {node.data} Min {min_value} Max {max_value}")

    if node.data < min_value or node.data > max_value:
        return False

    return check_bst(node.left, min_value, node.data) and \
        check_bst(node.right, node.data + 1, max_value)

def validate_bst(tree: Node):
    if not tree:
        return True # Valid

    return check_bst(tree.left, float('-inf'), tree.data) and \
        check_bst(tree.right, tree.data + 1, float('inf'))

tree = Node(8)
tree.left = Node(4)
tree.right = Node(10)
tree.left.left = Node(2)
tree.left.right = Node(6)
tree.right.right = Node(20)

assert validate_bst(tree) is True

tree = Node(8)
tree.left = Node(4)
tree.right = Node(10)
tree.left.left = Node(2)
tree.left.right = Node(12)
tree.right.right = Node(20)

assert validate_bst(tree) is False

tree = Node(8)
tree.left = Node(4)
tree.left.left = Node(2)
tree.right = Node(10)
tree.right.left = Node(9)
tree.right.left.left = Node(7)
tree.right.right = Node(20)

assert validate_bst(tree) is False
