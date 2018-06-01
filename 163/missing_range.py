def missing_range(s, high, low):
    h = set()
    res = []
    for x in s:
        h.add(x)
    for i in range(low, high + 1):
        if i not in h:
            res.append(i)
    return res


if __name__ == '__main__':
    s = [1, 14, 11, 51, 15]
    high = 55
    low = 50
    print missing_range(s, high, low)
