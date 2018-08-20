def helper(n, l):
    if n == 0:
        return ['']
    if n == 1:
        return ['0', '1', '8']
    temp = helper(n - 2, l)
    res = []
    for x in temp:
        if n != l:
            res.append('0' + x + '0')
        res.append('1' + x + '1')
        res.append('8' + x + '8')
        res.append('6' + x + '9')
        res.append('9' + x + '6')
    return res


def Strobogrammatic(n):
    return helper(n, n)


if __name__ == '__main__':
    n = 4
    print Strobogrammatic(n)
