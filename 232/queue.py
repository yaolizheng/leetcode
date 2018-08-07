class queue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.size = 0
        self.top = None

    def push(self, x):
        self.stack1.append(x)
        if self.size == 0:
            self.top = x
        self.size += 1

    def pop(self):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        rv = self.stack2.pop()
        if len(self.stack2) > 0:
            self.top = self.stack2.pop()
            self.stack1.append(self.top)
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        self.size -= 1
        return rv

    def peek(self):
        return self.top

    def empty(self):
        return self.size == 0


if __name__ == '__main__':
    q = queue()
    q.push(1)
    q.push(2)
    print q.peek()
    print q.pop()
    print q.empty()
