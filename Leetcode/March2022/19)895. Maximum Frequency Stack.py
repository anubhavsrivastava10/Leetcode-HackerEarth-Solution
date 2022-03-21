class FreqStack:

    def __init__(self):
        self.stack = []
        self.count = {}

    def push(self, val: int) -> None:
        if val not in self.count:
            self.count[val] = 1
        else:
            self.count[val] += 1
        if self.count[val] > len(self.stack):
            self.stack.append([val])
        else:
            self.stack[self.count[val]-1].append(val)

    def pop(self) -> int:
        while not self.stack[-1]:
            self.stack.pop()
        val = self.stack[-1].pop()
        self.count[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()