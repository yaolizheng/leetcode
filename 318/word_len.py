import sys


def word_len(l):
    mask = [0] * len(l)
    res = -sys.maxint + 1
    for i in range(len(l)):
        for c in l[i]:
            mask[i] |= 1 << (ord(c) - ord('a'))
        for j in range(0, i):
            if not (mask[i] & mask[j]):
                res = max(res, len(l[i]) * len(l[j]))
    return res


if __name__ == '__main__':
    l = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    print word_len(l)
