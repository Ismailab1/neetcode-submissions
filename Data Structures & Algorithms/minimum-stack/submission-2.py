class MinStack:

    def __init__(self):
        # Initailizes a stack for the values of the
        # array and the minstack for tracking the nth minimum val
        # at the nth size of the value array
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        # Adds the val to the current stack and checks if the current
        # val is lower than the minimum val at the nth position of the
        # minstack array
        self.stack.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        # Pushes the minimum value to the minimum array to call
        # at O(1) speed if needed
        self.minstack.append(val)

    def pop(self) -> None:
        # Pops the value stack and minimum stack to keep both
        # the top value and the minimum value accurate with
        # each other
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        # Checks the value at the top of the stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Checks the value at the top of the minimum stack
        return self.minstack[-1]
        
