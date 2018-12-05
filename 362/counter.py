class Counter():

    def __init__(self):
        self.q = list()

    def hit(self, n):
        self.q.append(n)

    def getHits(self, n):
        while len(self.q) > 0 and self.q[0] <= (n - 300):
            self.q.pop(0)
        return len(self.q)


if __name__ == '__main__':
    counter = Counter()
    counter.hit(1)
    counter.hit(2)
    counter.hit(3)
    print counter.getHits(4)
    counter.hit(300)
    print counter.getHits(300)
    print counter.getHits(301)
