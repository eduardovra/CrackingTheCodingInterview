
def compress_string(s: str) -> str:
    compressed: list = []
    cur_char = None
    cur_char_count = 0

    for c in s:
        if c == cur_char:
            cur_char_count += 1
        else:
            if cur_char_count:
                compressed.extend(f'{cur_char}{cur_char_count}')
            cur_char = c
            cur_char_count = 1

    if cur_char_count:
        compressed.extend(f'{cur_char}{cur_char_count}')

    return ''.join(compressed) if len(compressed) < len(s) else s

assert compress_string("aabcccccaaa") == "a2b1c5a3"
assert compress_string("abcc") == "abcc"
