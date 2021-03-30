from typing import Optional

class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
    
    def __repr__(self) -> str:
        return str(self.data)

def dfs(node, a, b):
    found = []

    if not node:
        return found

    if node.data == a:
        found.append(a)
    elif node.data == b:
        found.append(b)

    left = dfs(node.left, a, b)
    right = dfs(node.right, a, b)

    return [*found, *left, *right]

def first_common_ancestor(tree, a, b):
    if not tree:
        return None

    left = dfs(tree.left, a, b)
    if a in left and b in left:
        return first_common_ancestor(tree.left, a ,b)
    right = dfs(tree.right, a, b)
    if a in right and b in right:
        return first_common_ancestor(tree.right, a ,b)

    if a in left and b in right:
        return tree.data

    if a in right and b in left:
        return tree.data

    return None

tree = Node(1)

tree.left = Node(2)
tree.left.left = Node(3)
tree.left.left.left = Node(4)
tree.left.left.right = Node(5)

tree.right = Node(6)
tree.right.left = Node(7)
tree.right.right = Node(8)
tree.right.right.left = Node(9)
tree.right.right.right = Node(10)

assert first_common_ancestor(tree, 4, 10) == 1
assert first_common_ancestor(tree, 4, 5) == 3
assert first_common_ancestor(tree, 9, 7) == 6
assert first_common_ancestor(tree, 7, 10) == 6
assert first_common_ancestor(tree, 2, 7) == 1
