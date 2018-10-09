class Sum:

    def __init__(self, num):
        self.num = num
        for i in range(1, len(self.num)):
            self.num[i] += self.num[i - 1]

    def sum(self, i, j):
        return self.num[j] if i == 0 else self.num[j] - self.num[i - 1]


if __name__ == '__main__':
    n = [-2, 0, 3, -5, 2, -1]
    test = Sum(n)
    print test.sum(0, 5)
