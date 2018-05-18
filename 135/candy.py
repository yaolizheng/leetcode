def candy(l):
    n = len(l)
    l2r = [1] * n
    r2l = [1] * n
    sum = 0
    for i in range(1, n):
        if l[i] > l[i - 1]:
            l2r[i] = l2r[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if l[i] > l[i + 1]:
            r2l[i] = r2l[i + 1] + 1
    for i in range(n):
        sum += max(r2l[i], l2r[i])
    return sum


if __name__ == '__main__':
    l = [1, 0, 2]
    print candy(l)
