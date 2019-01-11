import sys


def guess_num(n):
    dp = [[0] * (n + 1) for x in range(n + 1)]
    for i in range(2, n + 1):
        for j in range(i - 1, 0, -1):
            _min = sys.maxint
            for k in range(j + 1, i):
                local_max = k + max(dp[j][k - 1], dp[k + 1][i])
                _min = min(_min, local_max)
            dp[j][i] = j if j + 1 == i else _min
    return dp[1][n]


if __name__ == '__main__':
    print guess_num(10)
