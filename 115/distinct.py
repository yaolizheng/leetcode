def distinct(s, t):
    m = len(s)
    n = len(t)
    dp = [[0] * (n + 1) for x in range(m + 1)]
    for x in range(m + 1):
        dp[x][0] = 1
    for x in range(1, n + 1):
        dp[0][x] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] != t[j - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
    return dp[m][n]


if __name__ == '__main__':
    s = 'babgbag'
    t = 'bag'
    print distinct(s, t)
