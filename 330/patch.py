def patch(l, n):
    miss = 1
    res = 0
    i = 0
    while miss <= n:
        if i < len(l) and l[i] <= miss:
            miss += l[i]
            i += 1
        else:
            miss += miss
            res += 1
    return res


if __name__ == '__main__':
    l = [1, 5, 10]
    n = 20
    print patch(l, n)
