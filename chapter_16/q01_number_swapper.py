
def get_bit(num, bit):
    return num & (1 << bit)

def set_bit(num, bit):
    return num | (1 << bit)

def clear_bit(num, bit):
    return num & ~(1 << bit)

def swap_numbers(a, b):
    for i in range(32):
        bit_a = get_bit(a, i)
        bit_b = get_bit(b, i)

        if bit_a and not bit_b:
            # Clear bit on a and set bit on b
            a = clear_bit(a, i)
            b = set_bit(b, i)
        elif bit_b and not bit_a:
            # Clear bit on b and set bit on a
            b = clear_bit(b, i)
            a = set_bit(a, i)

    return a, b

assert swap_numbers(12, 55) == (55, 12)
assert swap_numbers(-12, -55) == (-55, -12)
