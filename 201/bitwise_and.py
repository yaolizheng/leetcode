def len_bit(s):
    res = 0
    while s:
        s = s >> 1
        res += 1
    return res


def bitwise_and(n):
    a = n[0]
    b = n[1]
    res = 0
    while a > 0 and b > 0:
        len_a = len_bit(a) - 1
        len_b = len_bit(b) - 1
        if len_a != len_b:
            break
        res += 2 ** len_a
        a -= 2 ** len_a
        b -= 2 ** len_a
    return res


def bitwise_and2(n):
    a = n[0]
    b = n[1]
    i = 0
    while a != b:
        a >>= 1
        b >>= 1
        i += 1
    return a << i


if __name__ == '__main__':
    # n = [5, 7]
    n = [0, 1]
    print bitwise_and2(n)
