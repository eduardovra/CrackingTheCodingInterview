from typing import Optional, List


class Node:
    def __init__(self, key, item) -> None:
        self.key = key
        self.item = item
        self.next = None


class HashTable:
    def __init__(self) -> None:
        self.size = 3
        self.entries: List[Optional[Node]] = [None] * self.size

    def _hash(self, key):
        return sum(ord(c) for c in key)

    def _get(self, key):
        i = abs(self._hash(key)) % self.size

        node = self.entries[i]
        while node:
            if node.key == key:
                return node.item
            node = node.next

        raise KeyError("Not found")

    def _set(self, key, item):
        i = abs(self._hash(key)) % self.size

        if self.entries[i]:
            # Check if key already present
            node = self.entries[i]
            while node:
                if node.key == key:
                    node.item = item
                    return
                node = node.next

            # Key not present, create new node
            node = Node(key, item)
            node.next = self.entries[i]
            self.entries[i] = node
        else:
            self.entries[i] = Node(key, item)

    def __getitem__(self, key):
        return self._get(key)

    def __setitem__(self, key, item):
        self._set(key, item)


ht = HashTable()

ht["tom"] = 35
ht["josy"] = 27
ht["mike"] = 13
ht["olivia"] = 44

assert ht["tom"] == 35
assert ht["josy"] == 27
assert ht["mike"] == 13
assert ht["olivia"] == 44

pass
