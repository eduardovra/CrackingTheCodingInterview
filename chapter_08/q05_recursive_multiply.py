def recursive_multiply(a, b):
    if a == 0:
        return 0
    elif a == 1:
        return b

    return b + recursive_multiply(a - 1, b)

assert recursive_multiply(3, 5) == 15
assert recursive_multiply(7, 2) == 14
