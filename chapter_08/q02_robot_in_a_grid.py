from typing import List


def find_path(grid, row=0, col=0, path: List = []):
    rows = len(grid)
    cols = len(grid[0])

    print(f" Path {row}, {col}")

    # Boundary check
    if row >= rows or col >= cols:
        print(f"  boundary check")
        return []

    # If cell is off limits
    if not grid[row][col]:
        print(f"  offlimits")
        return []

    # Reached the end
    if row == rows - 1 and col == cols - 1:
        print(f"  reached end")
        return [(row, col)]

    # Try path to the right
    found = find_path(grid, row + 1, col, path)
    if found:
        return [(row, col)] + found

    # Try path bellow
    found = find_path(grid, row, col + 1, path)
    if found:
        return [(row, col)] + found

    print(f"  deadend")

    # Dead end
    return []


grid = [
    [True, False],
    [True, True],
]

print("Starting")
assert find_path(grid) == [(0, 0), (1, 0), (1, 1)]

grid = [
    [True, True, True],
    [True, False, True],
    [True, False, True],
]

print("Starting")
assert find_path(grid) == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

grid = [
    [True, True, False],
    [True, False, True],
    [True, True, True],
]

print("Starting")
assert find_path(grid) == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

grid = [
    [True, True, False, True],
    [False, True, False, True],
    [True, True, True, False],
    [True, False, True, True],
]

print("Starting")
assert find_path(grid) == [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3)]
