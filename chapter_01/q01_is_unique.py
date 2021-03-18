import sys

# O(n)
def is_unique(s: str) -> bool:
    array = [False] * sys.maxunicode

    for c in s:
        c_int = ord(c)

        if array[c_int]:
            return False

        array[c_int] = True

    return True

assert is_unique('abc') is True
assert is_unique('abb') is False
