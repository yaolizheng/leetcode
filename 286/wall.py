import sys


def helper(m, i, j, l):
    if i < 0 or i >= len(m) or j < 0 or j >= len(m[0]) or m[i][j] < l:
        return
    m[i][j] = l
    helper(m, i + 1, j, l + 1)
    helper(m, i - 1, j, l + 1)
    helper(m, i, j + 1, l + 1)
    helper(m, i, j - 1, l + 1)


def wall(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                helper(m, i, j, 0)
    return m


if __name__ == '__main__':
    m = [[sys.maxint, -1, 0, sys.maxint], [sys.maxint, sys.maxint, sys.maxint, -1], [sys.maxint, -1, sys.maxint, -1], [0, -1, sys.maxint, sys.maxint]]
    print wall(m)
