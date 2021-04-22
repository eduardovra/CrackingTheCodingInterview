
def find_magic_index(array, indexes=[]):
    if not array:
        # Magic index not found
        return None

    if not indexes:
        indexes = range(len(array))

    l = len(array)
    index = l // 2
    number = array[index]
    absolute_index = indexes[index]

    if number == absolute_index:
        return absolute_index
    elif number > absolute_index:
        # Look in the first half
        print(f"Looking first half {array[:index]} ranges {indexes[:index]}")
        return find_magic_index(array[:index], indexes[:index])
    else:
        # Look in the second half
        print(f"Looking second half {array[index:]} ranges {indexes[index:]}")
        return find_magic_index(array[index:], indexes[index:])

array = [1,1,1,2,3,5]

magic = find_magic_index(array)
print(magic)
assert magic == 5

array = [-10,-5,2,2,2,3,4,7,9,12,13]

magic = find_magic_index(array)
print(magic)
assert magic == 7
