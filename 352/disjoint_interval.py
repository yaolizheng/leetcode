class DisjointInterval:

    def __init__(self):
        self.interval = []

    def add(self, num):
        temp = []
        target = [num, num]
        pos = 0
        for i in range(len(self.interval)):
            current = self.interval[i]
            if current[1] + 1 < target[0]:
                temp.append(current)
            elif current[0] - 1 > target[1]:
                temp.append(current)
                pos += 1
            else:
                target = [min(current[0], target[0]), max(current[1], target[1])]
        temp.insert(pos, target)
        self.interval = temp

    def get(self):
        return self.interval


if __name__ == '__main__':
    test = DisjointInterval()
    test.add(1)
    print test.get()
    test.add(3)
    print test.get()
    test.add(7)
    print test.get()
    test.add(2)
    print test.get()
    test.add(6)
    print test.get()
