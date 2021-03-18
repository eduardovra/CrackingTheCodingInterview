import sys

# O(a + b)
def check_permutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    array = [0] * sys.maxunicode

    for c in s1:
        i = ord(c)
        array[i] += 1
    for c in s2:
        i = ord(c)
        array[i] -= 1

        if array[i] < 0:
            return False

    return True

assert check_permutation('abc', 'cba') is True
assert check_permutation('abc', 'abd') is False
