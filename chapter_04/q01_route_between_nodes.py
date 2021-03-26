from typing import List

class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.visited = False
        self.children: List[Node] = []

class Graph:
    def __init__(self, nodes) -> None:
        self.nodes = nodes

def is_there_route(graph: Graph, a: Node, b: Node) -> bool:
    # Start from a and try to reach b

    for node in graph.nodes:
        node.visited = False

    queue = list(a.children) # Using an list as a queue for simplicity
    while queue:
        node = queue.pop(0)
        if node.visited:
            continue

        node.visited = True
        if node is b:
            return True
        queue.extend(node.children)

    return False

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
g = Node('G')

a.children = [b, c, g]
b.children = [c, f]
c.children = [d, e]

graph = Graph([a, b, c, d, e, f, g])

assert is_there_route(graph, a, e) == True
assert is_there_route(graph, d, f) == False
assert is_there_route(graph, a, g) == True
assert is_there_route(graph, b, c) == True
assert is_there_route(graph, g, f) == False
assert is_there_route(graph, a, c) == True
