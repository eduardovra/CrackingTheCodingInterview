
# O(n)
def urlify(url: str, text_length: int) -> str:
    # Cast to list because python strings are immutable
    array: list = list(url)

    # To avoid using len we can count the spaces to determine
    # the actual size of the array
    spaces = 0
    for c in array[:text_length]:
        if c == ' ':
            spaces += 1
    
    # We already have room for 1 char of space so just have to add 2 more
    # to hold the %20 value
    array_length = text_length + spaces * 2
    dest_i = array_length - 1

    for src_i in range(text_length - 1, -1, -1):
        src_c = array[src_i]
        if src_c == ' ':
            array[dest_i - 2] = '%'
            array[dest_i - 1] = '2'
            array[dest_i] = '0'
            dest_i -= 3
        else:
            array[dest_i] = array[src_i]
            dest_i -= 1

    return ''.join(array)

assert urlify("Mr John Smith    ", 13) == "Mr%20John%20Smith"
