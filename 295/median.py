import heapq


class median():

    def __init__(self):
        self.small = list()
        self.large = list()

    def addNum(self, n):
        if len(self.small) == 0 or n <= self.small[0]:
            heapq.heappush(self.small, -n)
        else:
            heapq.heappush(self.large, n)

    def findMedian(self):
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]


if __name__ == '__main__':
    test = median()
    test.addNum(2)
    print test.findMedian()
    test.addNum(3)
    print test.findMedian()
    test.addNum(4)
    print test.findMedian()
