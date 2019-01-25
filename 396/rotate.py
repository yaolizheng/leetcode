def rotate(a, n):
    s = 0
    tmp = 0
    for i in range(n):
        s += a[i]
        tmp += i * a[i]
    res = tmp
    for i in range(1, n):
        tmp = tmp + s - n * a[n - i]
        res = max(res, tmp)
    return res


if __name__ == '__main__':
    a = [4, 3, 2, 6]
    n = 4
    print rotate(a, n)
