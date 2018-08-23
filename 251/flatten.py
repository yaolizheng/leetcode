class flattern:

    def __init__(self, x):
        self.x = x
        self.row = 0
        self.col = 0

    def next(self):
        while len(self.x[self.row]) == 0:
            self.row += 1
            self.col = 0
        res = self.x[self.row][self.col]
        if len(self.x[self.row]) == (self.col + 1):
            self.row += 1
            self.col = 0
        else:
            self.col += 1
        return res

    def hasNext(self):
        return self.row < len(self.x)


if __name__ == '__main__':
    x = [[], [1, 2], [], [3], [4, 5, 6]]
    f = flattern(x)
    while f.hasNext():
        print f.next()
