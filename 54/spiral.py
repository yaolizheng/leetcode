def spiral(t):
    i = 0
    j = len(t[0])
    m = len(t)
    n = 0
    res = []
    while m > i and j > n:
        for x in range(n, j):
            res.append(t[i][x])
        i += 1
        for x in range(i, m):
            res.append(t[x][j - 1])
        j -= 1
        if m > i:
            for x in range(j - 1, n - 1,  - 1):
                res.append(t[m - 1][x])
            m -= 1
        if j > n:
            for x in range(m - 1, i - 1, -1):
                res.append(t[x][n])
            n += 1
    return res


if __name__ == '__main__':
    t = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print spiral(t)
