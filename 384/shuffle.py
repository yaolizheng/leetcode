import random
import copy


class solustion:

    def __init__(self, l):
        self.l = l

    def reset(self):
        return self.l

    def shuffle(self):
        res = copy.copy(self.l)
        for i in range(len(self.l)):
            index = i + random.randint(0, len(res) - i - 1)
            res[i], res[index] = res[index], res[i]
        return res


if __name__ == '__main__':
    l = [1, 2, 3]
    test = solustion(l)
    print test.reset()
    print test.shuffle()
    print test.reset()
