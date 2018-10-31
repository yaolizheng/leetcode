def dfs(m, i, j, dp):
    if dp[i][j] != 0:
        return dp[i][j]
    max_l = 1
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for d in dir:
        x = i + d[0]
        y = j + d[1]
        if x >= len(m) or x < 0 or y >= len(m[0]) or y < 0 or m[x][y] <= m[i][j]:
            continue
        l = 1 + dfs(m, x, y, dp)
        max_l = max(max_l, l)
    dp[i][j] = max_l
    return dp[i][j]


def longest_path(m):
    dp = [[0] * len(m) for x in range(len(m[0]))]
    res = 1
    for i in range(len(m)):
        for j in range(len(m[0])):
            res = max(res, dfs(m, i, j, dp))
    return res


if __name__ == '__main__':
    m = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    print longest_path(m)
