from typing import Set

class Node:
    def __init__(self, project) -> None:
        self.project = project
        self.dependencies: Set[Node] = set()

    def __repr__(self) -> str:
        deps = [p.project for p in self.dependencies]
        return f"Project: {self.project} Dependencies: {deps}"

def build_order(projects, dependencies):
    order = []

    projects = {p: set() for p in projects}

    for d in dependencies:
        dep, proj = d
        projects[proj].add(dep)

    while True:
        # If projects list is empty, we're finished
        if not projects:
            break

        # Find projects with no dependencies
        no_deps = [proj for proj, deps in projects.items() if not deps]

        # If there's no projects without dependencies, solution is impossible
        if not no_deps:
            return None

        # Add them to the build list
        order.extend(no_deps)
        # Remove from the projects list
        for p in no_deps:
            del projects[p]
            # Remove it from any other project's dependency list
            for deps in projects.values():
                if p in deps:
                    deps.remove(p)

    print(f"Order: {order}")

    return order

projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
order = build_order(projects, dependencies)

assert order == ['e', 'f', 'a', 'b', 'd', 'c']
