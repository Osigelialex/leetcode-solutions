class MinStack:

    def __init__(self):
        self.minstack = []
        self.substack = []

    def push(self, val: int) -> None:
        if not self.substack:
            self.substack.append(val)
        else:
            if val <= self.substack[-1]:
                self.substack.append(val)
        self.minstack.append(val)

    def pop(self) -> None:
        if self.top() == self.substack[-1]:
            self.substack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.minstack[-1]

    def getMin(self) -> int:
        return self.substack[-1]