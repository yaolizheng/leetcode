def unique_paths2(grid):
    m = len(grid)
    n = len(grid[0])
    table = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                table[i][j] = 0
            elif i == 0:
                table[i][j] = 1
            elif j == 0:
                table[i][j] = 1
            else:
                table[i][j] = table[i - 1][j] + table[i][j - 1]
    return table[m - 1][n - 1]


if __name__ == '__main__':
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print unique_paths2(grid)
