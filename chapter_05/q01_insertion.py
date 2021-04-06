def get_bit(num, bit):
    return num & (1 << bit)

def set_bit(num, bit):
    return num | (1 << bit)


def clear_bit(num, bit):
    return num & ~(1 << bit)


def insertion(n, m, i, j):
    for i_bit in range(i, j + 1):
        bit = get_bit(n, i_bit - i)
        if bit:
            m = set_bit(m, i_bit)
        else:
            m = clear_bit(m, i_bit)

    return m

assert insertion(0b10011, 0b10000000000, 2, 6) == 0b10001001100
