def ballons(n):
    _len = len(n)
    n.append(1)
    n.insert(0, 1)
    print n
    dp = [[0] * len(n) for x in range(len(n))]
    for l in range(1, _len + 1):
        for i in range(1, _len - l + 2):
            j = i + l - 1
            for k in range(i, j + 1):
                dp[i][j] = max(dp[i][j], dp[i][k - 1] + dp[k + 1][j] + n[i - 1] * n[k] * n[j + 1])
    return dp[1][_len]


if __name__ == '__main__':
    n = [3, 1, 5, 8]
    print ballons(n)
