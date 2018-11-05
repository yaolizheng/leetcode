import sys


def has_triplet(l):
    m1 = sys.maxint
    m2 = sys.maxint
    for x in l:
        if m1 > x:
            m1 = x
        elif m2 > x:
            m2 = x
        else:
            return True
    return False


if __name__ == '__main__':
    l = [1, 2, 1]
    print has_triplet(l)
