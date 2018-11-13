class MovingAverage:

    def __init__(self, size):
        self.size = size
        self.q = []
        self.sum = 0.0

    def next(self, n):
        if len(self.q) >= self.size:
            self.sum -= self.q.pop(0)
        self.q.append(n)
        self.sum += n
        return self.sum / len(self.q)


if __name__ == '__main__':
    test = MovingAverage(3)
    print test.next(1)
    print test.next(10)
    print test.next(3)
    print test.next(5)
