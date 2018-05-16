import sys


def best_time(l):
    res = 0
    min = sys.maxint
    for x in l:
        if x < min:
            min = x
        if x > min:
            res = max(res, x - min)
    return res


if __name__ == '__main__':
    # l = [7, 1, 5, 3, 6, 4]
    l = [7, 6, 4, 3, 1]
    print best_time(l)
