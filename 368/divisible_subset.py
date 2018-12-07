def divisable_subset(n):
    dp = [0] * len(n)
    parents = [-1] * len(n)
    max_l = 0
    max_index = -1
    n.sort()
    for i in range(len(n), -1, -1):
        for j in range(i, len(n)):
            if n[j] % n[i] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                parents[i] = j
                if dp[i] > max_l:
                    max_l = dp[i]
                    max_index = i
    res = []
    for i in range(max_l):
        res.append(n[max_index])
        max_index = parents[max_index]
    return res


if __name__ == '__main__':
    n = [1, 2, 4, 8]
    print divisable_subset(n)
