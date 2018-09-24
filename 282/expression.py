def help(n, temp1, temp2, res, diff, t):
    if len(n) == 0 and temp1 == t:
        res.append(temp2)
    for i in range(1, len(n) + 1):
        num = n[:i]
        if len(num) > 0 and num[0] == 0:
            return
        next = n[i:]
        if len(temp2) > 0:
            help(next, temp1 + int(num), temp2 + '+' + num, res, int(num), t)
            help(next, temp1 - int(num), temp2 + '-' + num, res, -int(num), t)
            help(next, (temp1 - diff) + diff * int(num), temp2 + '*' + num, res, diff * int(num), t)
        else:
            help(next, int(num), num, res, int(num), t)


def expression(n, t):
    res = []
    temp1 = 0
    temp2 = ''
    diff = 0
    help(n, temp1, temp2, res, diff, t)
    return res


if __name__ == '__main__':
    n = "232"
    target = 8
    print expression(n, target)
