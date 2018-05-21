def single_int(l):
    res = 0
    for x in l:
        res ^= x
    return res


if __name__ == '__main__':
    l = [4, 1, 2, 1, 2]
    print single_int(l)
