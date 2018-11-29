def envelope(l):
    l.sort()
    dp = [1] * len(l)
    for i in range(len(l)):
        for j in range(i):
            if l[i][0] > l[j][0] and l[i][1] > l[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[-1]


if __name__ == '__main__':
    l = [[5, 4], [6, 4], [6, 7], [2, 3]]
    print envelope(l)
