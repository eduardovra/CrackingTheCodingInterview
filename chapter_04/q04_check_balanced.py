from typing import Optional


class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.visited = False

def check_height(tree: Optional[Node]):
    if not tree:
        return 0

    print(f"Inspecting node {tree.data}")

    left_height = check_height(tree.left)
    print(f"  Height below {tree.data}, left branch: {left_height}")
    if left_height is False:
        return False

    right_height = check_height(tree.right)
    print(f"  Height below {tree.data}, right branch: {right_height}")
    if right_height is False:
        return False

    if abs(left_height - right_height) > 1:
        return False

    return max(left_height + 1, right_height + 1)


def check_balanced(tree: Optional[Node]):
    return check_height(tree) is not False


tree = Node(1)
tree.left = Node(2)
tree.right = Node(5)
tree.left.left = Node(3)
tree.left.right = Node(4)
tree.right.right = Node(6)

assert check_balanced(tree) == True

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.right.left = Node(4)
tree.right.right = Node(5)

assert check_balanced(tree) == True

tree = Node(1)
tree.left = Node(2)
tree.right = Node(5)
tree.left.left = Node(3)
tree.left.right = Node(4)
tree.right.right = Node(6)
tree.right.right.left = Node(7)
tree.right.right.right = Node(9)
tree.right.right.left.left = Node(8)

assert check_balanced(tree) == False

tree = Node(1)
tree.left = Node(2)
tree.right = Node(6)
tree.left.left = Node(3)
tree.left.left.left = Node(4)
tree.left.left.right = Node(5)

assert check_balanced(tree) == False
