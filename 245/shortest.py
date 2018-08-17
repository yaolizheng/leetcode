import sys


def shortest(words, a, b):
    prev = -1
    res = sys.maxint
    for i in range(len(words)):
        w = words[i]
        if w == a or w == b:
            if prev != -1:
                res = min(res, abs(i - prev))
            prev = i
    return res


if __name__ == '__main__':
    words = ["practice", "makes", "perfect", "coding", "makes"]
    print shortest(words, "makes", "makes")
