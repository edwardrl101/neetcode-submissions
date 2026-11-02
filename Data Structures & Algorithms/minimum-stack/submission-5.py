class MinStack:

    def __init__(self):
        self.stack = []
        self.track = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.track or val <= self.track[-1]:
            self.track.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.track[-1]:
            self.track.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.track[-1]
        
