def helper(n, k, start, temp, res):
    if len(temp) == k:
        res.append(temp)
        return
    for i in range(start, n):
        helper(n, k, i + 1, temp + [i + 1], res)


def combinations(n, k):
    res = []
    helper(n, k, 0, [], res)
    return res


if __name__ == '__main__':
    n = 4
    k = 2
    print combinations(n, k)
