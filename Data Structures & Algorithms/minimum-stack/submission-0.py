class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minStack = val
        else:
            self.stack.append(val - self.minStack)
            if val < self.minStack:
                self.minStack = val

    def pop(self) -> None:
        if not self.stack:
            return
        
        pop = self.stack.pop()

        if pop < 0:
            self.minStack = self.minStack - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.minStack
        else:
            return self.minStack

    def getMin(self) -> int:
        return self.minStack
