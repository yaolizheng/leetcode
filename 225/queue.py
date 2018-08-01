class stack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        self.size = 0

    def push(self, x):
        self.queue1.append(x)
        self.size += 1

    def pop(self):
        for _ in range(0, self.size - 1):
            temp = self.queue1[0]
            del self.queue1[0]
            self.queue2.append(temp)
        rv = self.queue1[0]
        del self.queue1[0]
        self.queue1, self.queue2 = self.queue2, self.queue1
        self.size -= 1
        return rv

    def top(self):
        for i in range(0, self.size):
            temp = self.queue1[0]
            del self.queue1[0]
            self.queue2.append(temp)
        rv = self.queue1[0]
        del self.queue1[0]
        self.queue2.append(rv)
        return rv

    def empty(self):
        return self.size == 0


if __name__ == '__main__':
    s = stack()
    print s.empty()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)
    print s.pop()
    print s.pop()
    s.push(8)
    s.push(9)
    print s.pop()
    print s.pop()
    print s.empty()
