# Could use lru_cache for performance

def triple_step(n, cache=[]):
    if not cache:
        cache = [None] * (n + 1)

    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif cache[n] is not None:
        return cache[n]

    cache[n] = triple_step(n - 1, cache) + triple_step(n - 2, cache) + triple_step(n - 3, cache)

    return cache[n]


assert triple_step(1) == 1
assert triple_step(2) == 2
assert triple_step(3) == 4
assert triple_step(4) == 7
assert triple_step(5) == 13
