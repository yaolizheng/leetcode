def fill(i, j, m, n, t):
    if i < 0 or j < 0 or i > m - 1 or j > n - 1:
        return 0
    if t[i][j] == 'v' or t[i][j] == 0:
        return 0
    t[i][j] = 'v'
    return 1 + fill(i, j - 1, m, n, t) + fill(i - 1, j, m, n, t) + fill(i, j + 1, m, n, t) + fill(i + 1, j, m, n, t)


def islands(t):
    m = len(t)
    n = len(t[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if fill(i, j, m, n, t) > 0:
                count += 1
    return count


if __name__ == '__main__':
    table = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]
    print islands(table)
