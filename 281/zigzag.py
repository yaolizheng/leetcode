import sys


class zigzag():

    def __init__(self, l1, l2):
        self.queue = []
        self.queue.append(l1)
        self.queue.append(l2)
        self.i = 0
        self.j = 0

    def next(self):
        if self.i <= self.j:
            res = self.queue[0][self.i]
            self.i += 1
            if self.i == len(self.queue[0]):
                self.i = sys.maxint
        else:
            res = self.queue[1][self.j]
            self.j += 1
            if self.j == len(self.queue[1]):
                self.j = sys.maxint
        return res

    def hasNext(self):
        return self.i < len(self.queue[0]) or self.j < len(self.queue[1])


if __name__ == '__main__':
    l1 = [1, 2]
    l2 = [3, 4, 5, 6]
    test = zigzag(l1, l2)
    while test.hasNext():
        print test.next()
