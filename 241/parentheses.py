def ops(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b


def helper(l):
    if l in helper.cache:
        return helper.cache[l]
    res = []
    for i in range(0, len(l)):
        if l[i] in ['*', '+', '-']:
            l_result = helper(l[:i])
            r_result = helper(l[i + 1:])
            for x in l_result:
                for y in r_result:
                    res.append(ops(l[i], int(x), int(y)))
    if len(res) == 0:
        res.append(int(l))
    helper.cache[l] = res
    return res


def parenthese(l):
    helper.cache = dict()
    return helper(l)


if __name__ == '__main__':
    l = '2*3-4*5'
    print parenthese(l)
