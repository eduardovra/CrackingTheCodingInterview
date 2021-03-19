# O(n^2)
def zero_matrix(matrix: list) -> list:
    rows_to_zero = [False] * len(matrix)
    cols_to_zero = [False] * len(matrix[0])

    for i_row, row in enumerate(matrix):
        for i_col, col in enumerate(row):
            if col == 0:
                rows_to_zero[i_row], cols_to_zero[i_col] = True, True

    for i_row, row in enumerate(rows_to_zero):
        if row:
            for i_col in range(len(cols_to_zero)):
                matrix[i_row][i_col] = 0

    for i_col, col in enumerate(cols_to_zero):
        if col:
            for i_row in range(len(rows_to_zero)):
                matrix[i_row][i_col] = 0

    return matrix


assert zero_matrix([
    [1,2,3],
    [4,0,5],
]) == [
    [1,0,3],
    [0,0,0],
]

assert zero_matrix([
    [0,2,3],
    [4,1,5],
]) == [
    [0,0,0],
    [0,1,5],
]
