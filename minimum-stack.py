class MinStack:
    def __init__(self):
        self.stack = []
        self.min_indexes = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_indexes) == 0 or val <= self.stack[self.min_indexes[-1]]:
            self.min_indexes.append(len(self.stack) - 1)

    def pop(self) -> None:
        if len(self.stack) - 1 == self.min_indexes[-1]:
            self.min_indexes.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min_indexes[-1]]
