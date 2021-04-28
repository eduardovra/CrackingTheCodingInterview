def power_set(input_set):
    if not input_set:
        return [tuple()]

    sets = power_set(input_set[1:])
    new_sets = [s + (input_set[0],) for s in sets]

    return sets + new_sets

assert power_set(('a')) == [(), ('a',)]
assert power_set(('a', 'b')) == [(), ('b',), ('a',), ('b', 'a')]
assert power_set(('a', 'b', 'c')) == [(), ('c',), ('b',), ('c', 'b'), ('a',), ('c', 'a'), ('b', 'a'), ('c', 'b', 'a')]
