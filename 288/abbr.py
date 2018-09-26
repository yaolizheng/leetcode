class abbr():

    def __init__(self, d):
        self.map = {}
        for w in d:
            key = w[0] + str(len(w[1:-1])) + w[-1]
            if key not in self.map:
                self.map[key] = list()
            if w not in self.map[key]:
                self.map[key].append(w)

    def isUnique(self, w):
        key = w[0] + str(len(w[1:-1])) + w[-1]
        return key not in self.map or self.map[key].count(w) == len(self.map[key])


if __name__ == '__main__':
    d = ["deer", "door", "cake", "card"]
    test = abbr(d)
    print test.isUnique('dear')
    print test.isUnique('cart')
    print test.isUnique('cane')
    print test.isUnique('make')
