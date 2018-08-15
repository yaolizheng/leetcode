import sys


def shortest(s, w1, w2):
    res = m = n = sys.maxint
    for i in range(len(s)):
        if s[i] == w1:
            m = i
            res = min(res, abs(m - n))
        elif s[i] == w2:
            n = i
            res = min(res, abs(m - n))
    if m is sys.maxint or n is sys.maxint:
        return None
    return res


if __name__ == '__main__':
    s = ["practice", "makes", "perfect", "coding", "makes"]
    w1 = "coding"
    w2 = "practic"
    print shortest(s, w1, w2)
