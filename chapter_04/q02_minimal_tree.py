from typing import Optional

class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

def create_minimal_tree(elements) -> Optional[Node]:
    if not elements:
        return None

    if len(elements) == 2:
        mid_element = 0
        left = []
        right = [elements[1]]
    else:
        mid_element = len(elements) // 2
        left = elements[:mid_element]
        right = elements[mid_element + 1:]

    root = Node(elements[mid_element])
    root.left = create_minimal_tree(left)
    root.right = create_minimal_tree(right)

    return root

elements = [2,4,6,8,10,20]

tree = create_minimal_tree(elements)
print(tree)
