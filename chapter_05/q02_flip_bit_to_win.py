def get_binary(num):
    l = []

    mask = 1
    while mask <= num:
        if num & mask:
            l.insert(0, 1)
        else:
            l.insert(0, 0)

        mask = mask << 1

    return l


def count_ones(l):
    bit_flipped = False
    count = 0

    for n in l:
        if n == 1:
            count += 1
        else:
            if bit_flipped:
                return count
            else:
                bit_flipped = True
                count += 1

    return count


def longest_ones_sequence(num):
    b_num = get_binary(num)
    longest = 0

    for i in range(len(b_num)):
        l = count_ones(b_num[i:])
        if l > longest:
            longest = l

    return longest


assert longest_ones_sequence(1775) == 8
