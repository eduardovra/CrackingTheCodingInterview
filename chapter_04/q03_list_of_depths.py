from typing import Optional


class LinkedListNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.visited = False


def list_of_depths(tree, depths = {}, depth = 0) -> dict:
    if tree is None or tree.visited:
        return depths

    tree.visited = True

    if depth in depths:
        node = depths[depth]
        # Find last node in the linked list
        while node and node.next:
            node = node.next
        node.next = LinkedListNode(tree.data)
    else:
        depths[depth] = LinkedListNode(tree.data)

    list_of_depths(tree.left, depths, depth + 1)
    list_of_depths(tree.right, depths, depth + 1)

    return depths

tree = Node(8)
tree.left = Node(4)
tree.left.left = Node(2)
tree.left.right = Node(6)

tree.right = Node(10)
tree.right.right = Node(20)

depths = list_of_depths(tree)

assert len(depths) == 3

assert depths[0].value == 8
assert depths[0].next is None

assert depths[1].value == 4
assert depths[1].next.value == 10
assert depths[1].next.next is None

assert depths[2].value == 2
assert depths[2].next.value == 6
assert depths[2].next.next.value == 20
assert depths[2].next.next.next is None
