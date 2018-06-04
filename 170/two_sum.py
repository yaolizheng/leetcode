class TwoSum:

    def __init__(self):
        self.l = set()

    def add(self, n):
        self.l.add(n)

    def find(self, s):
        for x in self.l:
            if s - x in self.l:
                return True
        return False


if __name__ == '__main__':
    test = TwoSum()
    test.add(1)
    test.add(3)
    test.add(5)
    print test.find(4)
    print test.find(7)
