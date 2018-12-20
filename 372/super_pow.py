def super_pow(a, b):
    res = 1
    for i in range(len(b)):
        res = pow(res, 10) * pow(a, b[i]) % 1337
    return res


def pow(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a % 1337
    half = pow(a % 1337, b / 2)
    if b % 2 == 0:
        return half * half % 1337
    return a * half * half % 1337


if __name__ == '__main__':
    a = 2
    b = [1, 0]
    print super_pow(a, b)
