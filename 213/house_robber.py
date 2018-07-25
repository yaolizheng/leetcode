def rob(n):
    l = len(n)
    dp = [0] * l
    dp[0] = n[0]
    dp[1] = max(n[0], n[1])
    for i in range(2, l):
        dp[i] = max(dp[i - 2] + n[i], dp[i - 1])
    return dp[-1]


def house_robber(n):
    l = len(n)
    if l == 1:
        return n[0]
    elif l == 2:
        return max(n[0], n[1])
    else:
        return max(rob(n[1:]), rob(n[:-1]))


if __name__ == '__main__':
    n = [1, 2, 3, 1]
    print house_robber(n)
