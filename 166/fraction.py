def fraction(n, d):
    res = ''
    if n / d < 0:
        res += '-'
    if n % d == 0:
        return str(n / d)
    table = {}
    res += str(n / d)
    res += '.'
    n = n % d
    i = len(res)
    while n != 0:
        if n not in table:
            table[n] = i
        else:
            i = table[n]
            res = res[:i] + '(' + res[i:] + ')'
            return res
        n = n * 10
        res += str(n / d)
        n = n % d
        i += 1
    return res


if __name__ == '__main__':
    n = 1
    d = 8
    print fraction(n, d)
