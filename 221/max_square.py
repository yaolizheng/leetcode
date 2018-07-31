def max_square(x):
    m = len(x)
    n = len(x[0])
    table = [[0] * (n + 1) for i in range(m + 1)]
    max_len = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1][j - 1] == 1:
                table[i][j] = min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1]) + 1
                max_len = max(max_len, table[i][j])
    return max_len * max_len


if __name__ == '__main__':
    x = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]
    print max_square(x)
