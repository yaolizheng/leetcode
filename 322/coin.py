import sys


def coin(c, n):
    dp = [sys.maxint] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(len(c)):
            if c[j] <= i:
                dp[i] = min(dp[i], dp[i - c[j]] + 1)
    return -1 if dp[n] == sys.maxint else dp[n]


if __name__ == '__main__':
    c = [15]
    n = 11
    print coin(c, n)
