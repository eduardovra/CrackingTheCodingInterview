from typing import Optional


class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __repr__(self) -> str:
        return str(self.data)


def match_tree(t1, t2):
    # Finished comparing the whole trees
    if not t1 and not t2:
        return True
    # Both trees must end at the same time
    elif (t1 and not t2) or (t2 and not t1):
        return False
    elif t1.data != t2.data:
        return False

    return match_tree(t1.left, t2.left) and match_tree(t1.right, t2.right)


def traverse(t1, t2):
    """Pre order traversal"""
    if not t1:
        return False
    elif t1.data == t2.data and match_tree(t1, t2):
        return True
    elif traverse(t1.left, t2) or traverse(t1.right, t2):
        return True

    return False


def is_subtree(t1, t2):
    """Returns True if T2 is a subtree of T1"""

    # Traverse T1, if a node is equal to t2 root node, compare
    # every node in the subtree
    return traverse(t1, t2)


t1 = Node(8)
t1.left = Node(4)
t1.right = Node(10)
t1.left.left = Node(2)
t1.left.right = Node(6)
t1.right.right = Node(20)

t2 = Node(4)
t2.left = Node(2)
t2.right = Node(6)

assert is_subtree(t1, t2) is True

t2 = Node(10)
t2.right = Node(20)

assert is_subtree(t1, t2) is True

t2 = Node(5)
t2.left = Node(2)
t2.right = Node(6)

assert is_subtree(t1, t2) is False

t2 = Node(4)
t2.left = Node(2)
t2.right = Node(5)

assert is_subtree(t1, t2) is False
