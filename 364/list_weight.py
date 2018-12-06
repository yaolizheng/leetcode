def helper(n, level, res):
    if type(n) is int:
        if level >= len(res):
            res.append(0)
        res[level] += n
    else:
        for x in n:
            helper(x, level + 1, res)


def list_weight(l):
    res = [0]
    for n in l:
        helper(n, 0, res)
    weight = 0
    for i in range(len(res)):
        weight += res[i] * (len(res) - i)
    return weight


if __name__ == '__main__':
    l = [1, [4, [6]]]
    print list_weight(l)
