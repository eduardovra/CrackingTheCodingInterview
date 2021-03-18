# O(n)
def one_away(str_a: str, str_b: str) -> bool:
    str_a_len = len(str_a)
    str_b_len = len(str_b)

    # If the difference in size is more than 1, then it's false
    diff = abs(str_a_len - str_b_len)
    if diff > 1:
        return False

    if str_a_len == str_b_len:
        # Check for modified characters
        modified = 0
        for i in range(str_a_len):
            if str_a[i] != str_b[i]:
                modified += 1
        return modified <= 1

    elif str_a_len > str_b_len:
        i_a = 0
        i_b = 0
        differences = 0
        while i_a < str_a_len and i_b < str_b_len:
            if str_a[i_a] != str_b[i_b]:
                differences += 1
                i_a += 1
            else:
                i_a += 1
                i_b += 1

    else:
        i_a = 0
        i_b = 0
        differences = 0
        while i_a < str_a_len and i_b < str_b_len:
            if str_a[i_a] != str_b[i_b]:
                differences += 1
                i_b += 1
            else:
                i_a += 1
                i_b += 1

    return differences <= 1

assert one_away("pale", "ple") is True
assert one_away("pales", "pale") is True
assert one_away("pale", "bale") is True
assert one_away("pale", "bake") is False
assert one_away("pale", "pam") is False
