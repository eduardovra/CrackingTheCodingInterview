
class TripleStack:
    def __init__(self) -> None:
        self.array = [None] * 9
        self.boundaries = {
            0: [0, int(len(self.array) / 3 - 1)],
            1: [int(len(self.array) / 3), int(2 * len(self.array) / 3 - 1)],
            2: [int(2 * len(self.array) / 3), len(self.array) - 1],
        }
        self.pointers = [
            self.boundaries[0][0],
            self.boundaries[1][0],
            self.boundaries[2][0],
        ]

    def push(self, stack, value):
        start, end = self.boundaries[stack]
        top = self.pointers[stack]
        if top > end:
            raise RuntimeError("Out of space")

        self.array[top] = value
        self.pointers[stack] = top + 1

    def pop(self, stack):
        start, end = self.boundaries[stack]
        top = self.pointers[stack]
        if top == start:
            raise RuntimeError("Stack empty")

        self.pointers[stack] = top - 1
        return self.array[top - 1]


stack = TripleStack()

stack.push(0, 10)
stack.push(0, 20)
stack.push(0, 30)
stack.push(1, 40)
stack.push(1, 50)
stack.push(1, 60)
stack.push(2, 70)
stack.push(2, 80)
stack.push(2, 90)

assert stack.pop(0) == 30
assert stack.pop(0) == 20
assert stack.pop(0) == 10
assert stack.pop(1) == 60
assert stack.pop(1) == 50
assert stack.pop(1) == 40
assert stack.pop(2) == 90
assert stack.pop(2) == 80
assert stack.pop(2) == 70
