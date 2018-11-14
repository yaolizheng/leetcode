def intersection(a, b):
    mapping = dict()
    res = list()
    for x in a:
        if x not in mapping:
            mapping[x] = 0
        mapping[x] += 1
    for x in b:
        if x in mapping:
            if mapping[x] > 0:
                res.append(x)
            mapping[x] -= 1
    return res


if __name__ == '__main__':
    a = [4, 9, 5]
    b = [9, 4, 9, 8, 4]
    print intersection(a, b)
