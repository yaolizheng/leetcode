class flatten:

    def __init__(self, l):
        self.q = l

    def hasNext(self):
        return len(self.q)

    def next(self):
        top = self.q.pop(0)
        if type(top) is int:
            return top
        for i in range(len(top) - 1, 0, -1):
            self.q.insert(0, top[i])
        return top[0]


if __name__ == '__main__':
    l = [[1, 1], 2, [1, 1]]
    test = flatten(l)
    while test.hasNext():
        print test.next()
