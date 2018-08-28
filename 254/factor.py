def helper(n, start, temp, res):
    if n == 1:
        if len(temp) > 1:
            res.append(temp)
    else:
        for i in range(start, n + 1):
            if n % i == 0:
                helper(n / i, i, temp + [i], res)


def factor(n):
    temp = []
    res = []
    helper(n, 2, temp, res)
    return res


if __name__ == '__main__':
    n = 8
    print factor(n)
