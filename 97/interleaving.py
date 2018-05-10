def helper(a, b, c, l, m, n):
    if len(a) == l and len(b) == m and len(c) == n:
        return True
    if (n == len(c) and (l < len(a) or m < len(b))):
        return False
    return (l < len(a) and a[l] == c[n] and helper(a, b, c, l + 1, m, n + 1)) or (m < len(b) and b[m] == c[n] and helper(a, b, c, l, m + 1, n + 1))


def interleaving(a, b, c):
    return helper(a, b, c, 0, 0, 0)


def interleaving2(a, b, c):
    m = len(a)
    n = len(b)
    if (m + n) != len(c):
        return False
    dp = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 and j == 0:
                dp[i][j] = True
            elif i == 0 and b[j - 1] == c[j - 1]:
                dp[i][j] = dp[i][j - 1]
            elif j == 0 and a[i - 1] == c[i - 1]:
                dp[i][j] = dp[i - 1][j]
            elif a[i - 1] == c[i + j - 1] and b[j - 1] != c[i + j - 1]:
                dp[i][j] = dp[i - 1][j]
            elif a[i - 1] != c[i + j - 1] and b[j - 1] == c[i + j - 1]:
                dp[i][j] = dp[i][j - 1]
            elif a[i - 1] == c[i + j - 1] and b[j - 1] == c[i + j - 1]:
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
    return bool(dp[m][n])


if __name__ == '__main__':
    a = 'aabcc'
    b = 'dbbca'
    c = 'aadbbcbcac'
    print interleaving2(a, b, c)
