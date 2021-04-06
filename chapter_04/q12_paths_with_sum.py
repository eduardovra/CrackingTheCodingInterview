from typing import Optional

class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __repr__(self) -> str:
        return str(self.data)

def sum_tree(node, value, acc):
    if not node:
        return 0

    times = 0
    acc += node.data
    if acc == value:
        times += 1

    times += sum_tree(node.left, value, acc)
    times += sum_tree(node.right, value, acc)

    return times

def paths_with_sum(tree, value):
    # Traverse tree, starting from the root node,
    # and return how many times the sum of elements
    # adds up to value
    if not tree:
        return 0

    paths = sum_tree(tree, value, 0)
    paths += paths_with_sum(tree.left, value)
    paths += paths_with_sum(tree.right, value)

    return paths

tree = Node(8)

assert paths_with_sum(tree, 8) == 1

tree.left = Node(4)
tree.right = Node(10)
tree.left.left = Node(2)
tree.left.right = Node(6)
tree.right.right = Node(20)

assert paths_with_sum(tree, 18) == 2
