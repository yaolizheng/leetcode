def bomb(grid):
    m = len(grid)
    n = len(grid[0])
    l1 = [[0] * n for x in range(m)]
    l2 = [[0] * n for x in range(m)]
    l3 = [[0] * n for x in range(m)]
    l4 = [[0] * n for x in range(m)]
    for i in range(m):
        for j in range(n):
            tmp = 0 if j == 0 or grid[i][j] == 'W' else l1[i][j - 1]
            l1[i][j] = tmp + 1 if grid[i][j] == 'E' else tmp
        for j in range(n - 1, -1, -1):
            tmp = 0 if j == n - 1 or grid[i][j] == 'W' else l2[i][j + 1]
            l2[i][j] = tmp + 1 if grid[i][j] == 'E' else tmp
    for j in range(n):
        for i in range(m):
            tmp = 0 if i == 0 or grid[i][j] == 'W' else l3[i - 1][j]
            l3[i][j] = tmp + 1 if grid[i][j] == 'E' else tmp
        for i in range(m - 1, -1, -1):
            tmp = 0 if i == m - 1 or grid[i][j] == 'W' else l4[i + 1][j]
            l4[i][j] = tmp + 1 if grid[i][j] == 'E' else tmp
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '0':
                res = max(res, l1[i][j] + l2[i][j] + l3[i][j] + l4[i][j])
    return res


if __name__ == '__main__':
    m = [['0', 'E', '0', '0'], ['E', '0', 'W', 'E'], ['0', 'E', '0', '0']]
    print bomb(m)
