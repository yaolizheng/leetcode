class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val):
        min_value = min(self.top(), val) if len(self.stack) > 0 else val
        self.stack.append((val, min_value))

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]

    def pop(self):
        del self.stack[-1]


if __name__ == '__main__':
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print stack.getMin()
    stack.pop()
    print stack.top()
    print stack.getMin()
