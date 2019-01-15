class Directory:

    def __init__(self, num):
        self.max_num = num
        self.used = [False] * self.max_num
        self.recycle = []
        self._next = 0

    def get(self):
        if self._next >= self.max_num and len(self.recycle) == 0:
            return -1
        if len(self.recycle) > 0:
            num = self.recycle.pop(0)
            self.used[num] = True
            return num
        rv = self._next
        self._next += 1
        self.used[rv] = True
        return rv

    def check(self, num):
        return not self.used[num] and num >= 0 and num <= self.max_num

    def release(self, num):
        if num >= 0 and num <= self.max_num and self.used[num] is True:
            self.recycle.append(num)
            self.used[num] = False


if __name__ == '__main__':
    test = Directory(10)
    print test.get()
    print test.get()
    print test.check(2)
    print test.get()
    print test.check(2)
    test.release(2)
    print test.check(2)
    print test.get()
