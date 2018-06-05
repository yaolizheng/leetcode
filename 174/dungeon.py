import sys


def dungeon(l):
    m = len(l)
    n = len(l[0])
    table = [[sys.maxint] * (n + 1) for x in range(m + 1)]
    table[m][n - 1] = table[m - 1][n] = 1
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            temp = min(table[i + 1][j], table[i][j + 1]) - l[i][j]
            table[i][j] = temp if temp > 0 else 1
    return table[0][0]


if __name__ == '__main__':
    l = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    print dungeon(l)
