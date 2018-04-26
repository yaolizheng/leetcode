def min_path_sum(grid):
    m = len(grid)
    n = len(grid[0])
    table = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                table[i][j] = grid[i][j]
            elif i == 0:
                table[i][j] = table[i][j - 1] + grid[i][j]
            elif j == 0:
                table[i][j] = table[i - 1][j] + grid[i][j]
            else:
                table[i][j] = min(table[i - 1][j], table[i][j - 1]) + grid[i][j]
    return table[m - 1][n - 1]


if __name__ == '__main__':
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print min_path_sum(grid)
