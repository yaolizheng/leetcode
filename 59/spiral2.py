def spiral2(n):
    res = [[0] * n for i in range(n)]
    fill = 1
    l = n - 1
    i = j = 0
    while fill <= n ** 2:
        if l == 0:
            res[i][j] = fill
            break
        for _ in range(l):
            res[i][j] = fill
            fill += 1
            j += 1
        for _ in range(l):
            res[i][j] = fill
            fill += 1
            i += 1
        for _ in range(l):
            res[i][j] = fill
            fill += 1
            j -= 1
        for _ in range(l):
            res[i][j] = fill
            fill += 1
            i -= 1
        l -= 2
        i += 1
        j += 1
        if fill > n ** 2:
            break
    return res


if __name__ == '__main__':
    print spiral2(3)
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
