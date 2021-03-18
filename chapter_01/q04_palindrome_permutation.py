
# O(n)
def palindrome_permutation(s: str) -> bool:
    array = [0] * 128

    for c in s:
        i = ord(c)

        if ord('a') <= i <= ord('z'):
            i -= ord('a')
        elif ord('A') <= i <= ord('Z'):
            i -= ord('A')
        else:
            continue

        array[i] += 1

    odd_chars = 0

    for i, c in enumerate(array):
        # Check if we have an odd quantitiy of this char
        if c % 2 != 0:
            if odd_chars:
                return False
            else:
                odd_chars += 1

    return odd_chars <= 1

assert palindrome_permutation("Tact Coa") is True
assert palindrome_permutation("taco cat") is True
assert palindrome_permutation("atco cta") is True
assert palindrome_permutation("Tac Coa") is False
