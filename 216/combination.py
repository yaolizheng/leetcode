def back_tracking(res, l, n, k, start):
    if sum(l) > n:
        return
    if len(l) > k:
        return
    if sum(l) == n and len(l) == k:
        res.append(l)
        return
    for i in range(start, 10):
        back_tracking(res, l + [i], n, k, i + 1)


def combination(k, n):
    res = list()
    back_tracking(res, [], n, k, 1)
    return res


if __name__ == '__main__':
    k = 3
    n = 9
    print combination(k, n)
