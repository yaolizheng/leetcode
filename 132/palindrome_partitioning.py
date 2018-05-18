import sys


def palindrome_partitioning(s):
    l = len(s)
    dp = [[0] * l for i in range(l)]
    is_valid = [[False] * l for i in range(l)]
    for i in range(l):
        dp[i][i] = 0
        is_valid[i][i] = True
    for l in range(2, len(s) + 1):
        for i in range(len(s) - l + 1):
            j = l + i - 1
            if l == 2:
                is_valid[i][j] = (s[i] == s[j])
            else:
                is_valid[i][j] = ((s[i] == s[j]) and is_valid[i + 1][j - 1])
            if is_valid[i][j]:
                dp[i][j] = 0
            else:
                dp[i][j] = sys.maxint
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + 1)
    return dp[0][l - 1]


if __name__ == '__main__':
    s = "aa"
    print palindrome_partitioning(s)
