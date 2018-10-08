def lis(l):
    dp = [1] * len(l)
    res = 1
    for i in range(len(l)):
        for j in range(i):
            if l[i] > l[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        res = max(res, dp[i])
    return res


def lis2(l):
    end = []
    end.append(l[0])
    for i in range(1, len(l)):
        x = l[i]
        if x < end[0]:
            end[0] = x
        elif x > end[-1]:
            end.append(x)
        else:
            a = 0
            b = len(end) - 1
            while a < b:
                mid = (a + b) / 2
                if x > end[mid]:
                    a = mid + 1
                else:
                    b = mid
            end[b] = x
    return len(end)


if __name__ == '__main__':
    l = [10, 9, 2, 5, 3, 7, 101, 18]
    print lis2(l)
