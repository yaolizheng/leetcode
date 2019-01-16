import random


class RandomizedSet:

    def __init__(self):
        self.mapping = dict()
        self.l = []

    def insert(self, val):
        if val not in self.mapping:
            self.mapping[val] = list()
        self.l.append(val)
        self.mapping[val].append(len(self.l) - 1)

    def remove(self, val):
        if val in self.mapping:
            index = self.mapping[val].pop(0)
            self.l[index], self.l[-1] = self.l[-1], self.l[index]
            del self.l[-1]
        else:
            return False

    def getRandom(self):
        return random.choice(self.l)


if __name__ == '__main__':
    test = RandomizedSet()
    test.insert(1)
    print test.remove(2)
    test.insert(2)
    print test.getRandom()
    print test.getRandom()
    print test.getRandom()
    print test.getRandom()
    print test.getRandom()
    print test.getRandom()
    print test.getRandom()
    print test.getRandom()
    print test.getRandom()
    print test.getRandom()
    test.remove(1)
    test.insert(2)
    print test.getRandom()
    print test.getRandom()
    print test.getRandom()
    print test.getRandom()
