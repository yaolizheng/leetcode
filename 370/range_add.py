def range_add(updates, l):
    res = [0] * (l + 1)
    for x in updates:
        res[x[0]] += x[2]
        res[x[1] + 1] -= x[2]
    for i in range(1, l + 1):
        res[i] += res[i - 1]
    del res[-1]
    return res


if __name__ == '__main__':
    updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
    l = 5
    print range_add(updates, l)
