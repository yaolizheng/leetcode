def sorted_transformed(l, a, b, c):
    n = len(l)
    res = [0] * n
    i = 0
    j = n - 1
    index = n - 1 if a >= 0 else 0
    while i <= j:
        if a >= 0:
            _l = cal(l[i], a, b, c)
            _r = cal(l[j], a, b, c)
            if _l >= _r:
                res[index] = _l
                i += 1
            else:
                res[index] = _r
                j -= 1
            index -= 1
        else:
            _l = cal(l[i], a, b, c)
            _r = cal(l[j], a, b, c)
            if _l < _r:
                res[index] = _l
                i += 1
            else:
                res[index] = _r
                j -= 1
            index += 1
    return res


def cal(n, a, b, c):
    return a * n * n + b * n + c


if __name__ == '__main__':
    l = [-4, -2, 2, 4]
    a = 1
    b = 3
    c = 5
    print sorted_transformed(l, a, b, c)
