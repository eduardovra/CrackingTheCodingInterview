class CircularArray:
    def __init__(self, size) -> None:
        self._items = [None] * size
        self._head = 0

    def __repr__(self) -> str:
        return repr(list(self))

    def __len__(self):
        return len(self._items)

    def __getitem__(self, position):
        if position >= len(self):
            raise IndexError

        i = self._head + position
        if i >= len(self):
            i -= len(self)
        return self._items[i]

    def __setitem__(self, position, item):
        if position >= len(self):
            raise IndexError

        i = self._head + position
        if i >= len(self):
            i -= len(self)
        self._items[i] = item

    def __iter__(self):
        self._iter = 0
        return self

    def __next__(self):
        if self._iter >= len(self):
            raise StopIteration

        item = self[self._iter]
        self._iter += 1
        return item

    def rotate(self, shift_right):
        if shift_right >= len(self):
            shift_right = shift_right % len(self)

        self._head -= shift_right
        if self._head < 0:
            self._head += len(self)

array = CircularArray(4)
array[0] = 0
array[1] = 1
array[2] = 2
array[3] = 3

array.rotate(1)
array.rotate(1)
array.rotate(1)
array.rotate(1)
array.rotate(8)
array.rotate(5)
