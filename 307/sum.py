class RangeSum:

    def __init__(self, num):
        self.num = num
        self.sum = list()
        for x in num:
            self.sum.append(x)
        for i in range(1, len(self.sum)):
            self.sum[i] += self.sum[i - 1]

    def update(self, i, v):
        diff = v - self.num[i]
        for i in range(i, len(self.sum)):
            self.sum[i] += diff
        self.num[i] = v

    def sumRange(self, start, end):
        return self.sum[end] if start == 0 else self.sum[end] - self.sum[start - 1]


if __name__ == '__main__':
    num = [1, 3, 5]
    test = RangeSum(num)
    print test.sumRange(0, 2)
    test.update(1, 2)
    print test.sumRange(0, 2)
