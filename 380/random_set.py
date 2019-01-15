import random


class RandomizedSet:

    def __init__(self):
        self.mapping = dict()

    def insert(self, val):
        self.mapping[val] = None

    def remove(self, val):
        if val in self.mapping:
            del self.mapping[val]
        else:
            return False

    def getRandom(self):
        return random.choice(self.mapping.keys())


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
