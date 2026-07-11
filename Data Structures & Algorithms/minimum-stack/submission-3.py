class MinStack:

    def __init__(self):
        self.stack = []
        self.s = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.s or val <= self.s[-1]:
            self.s.append(val)
        

    def pop(self) -> None:
        if self.stack.pop() == self.s[-1]:
            self.s.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.s[-1]
        
