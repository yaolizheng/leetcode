def missing(l):
    res = len(l)
    for i in range(len(l)):
        res ^= (l[i] ^ i)
    return res


if __name__ == '__main__':
    l = [3, 4, 1, 0]
    print missing(l)
