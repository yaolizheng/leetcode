def unique_paths(m, n):
    table = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0:
                table[i][j] = 1
            elif j == 0:
                table[i][j] = 1
            else:
                table[i][j] = table[i - 1][j] + table[i][j - 1]
    return table[m - 1][n - 1]


if __name__ == '__main__':
    m = 7
    n = 3
    print unique_paths(m, n)
