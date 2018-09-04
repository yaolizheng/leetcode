def single(n):
    res = 0
    a = 0
    b = 0
    for x in n:
        res ^= x
    diff = res & -res
    for x in n:
        if x & diff:
            a ^= x
        else:
            b ^= x
    return[a, b]


if __name__ == '__main__':
    n = [1, 2, 1, 3, 2, 5]
    print single(n)
