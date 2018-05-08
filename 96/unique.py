def unique_bst(n):
    res = [0] * (n + 1)
    res[0] = 1
    res[1] = 1
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            res[i] += res[j - 1] * res[i - j]
    return res[n]


if __name__ == '__main__':
    n = 3
    print unique_bst(n)
