import sys


def min_size(l, s):
    start = 0
    _sum = 0
    result = sys.maxint
    for end in range(0, len(l)):
        _sum += l[end]
        while _sum >= s:
            result = min(result, end - start + 1)
            _sum -= l[start]
            start += 1
    return result if result != sys.maxint else 0


if __name__ == '__main__':
    l = [2, 3, 1, 2, 4, 3, 7]
    s = 7
    print min_size(l, s)
