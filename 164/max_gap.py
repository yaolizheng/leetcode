def max_gap(l):
    if len(l) < 2:
        return 0
    max_l = max(l)
    min_l = min(l)
    b_l = (max_l - min_l) / len(l)
    b = []
    for _ in range((max_l - min_l) / b_l + 1):
        b.append([-1000, 1000])
    for x in l:
        index = (x - min_l) / b_l
        if x > b[index][0]:
            b[index][0] = x
        if x < b[index][1]:
            b[index][1] = x
    res = 0
    b = [x for x in b if x != [-1000, 1000]]
    for i in range(1, len(b)):
        res = max(res, b[i][0] - b[i - 1][1])
    return res


if __name__ == '__main__':
    l = [3, 6, 9, 1, 100, 2]
    print max_gap(l)
