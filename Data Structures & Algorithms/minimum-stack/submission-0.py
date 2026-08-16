class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        current_minimum = self.minimums[-1] if self.minimums else float('inf')
        if val < current_minimum:
            self.minimums.append(val)
        else:
            self.minimums.append(current_minimum)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minimums.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimums[-1]
        
