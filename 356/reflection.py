import sys


def reflection(points):
    mapping = dict()
    maxx = -sys.maxint + 1
    minx = sys.maxint
    for p in points:
        maxx = max(maxx, p[0])
        minx = min(minx, p[0])
        if float(p[0]) not in mapping:
            mapping[float(p[0])] = []
        mapping[float(p[0])].append(float(p[1]))
    mid = (maxx + minx) / 2.0
    for p in points:
        _p = mid * 2 - p[0]
        if _p not in mapping or p[1] not in mapping[_p]:
            return False
    return True


if __name__ == '__main__':
    points = [[1, 1], [-1, 1]]
    print reflection(points)
