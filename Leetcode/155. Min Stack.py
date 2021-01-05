class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []

    def push(self, x: int) -> None:
        self.lst.append(x)

    def pop(self) -> None:
        self.lst.pop()

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return min(self.lst)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()