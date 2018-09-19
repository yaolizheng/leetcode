def paint(n, k):
    if n == 0:
        return 0
    same = 0
    diff = k
    for i in range(2, n + 1):
        tmp = diff
        diff = (same + diff) * (k - 1)
        same = tmp * 1
    return same + diff


if __name__ == '__main__':
    n = 10
    k = 2
    print paint(n, k)
