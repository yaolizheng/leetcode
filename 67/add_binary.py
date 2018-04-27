def add(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]


def add2(a, b):
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    res = []
    while i >= 0 or j >= 0 or carry:
        m = 0 if i < 0 else int(a[i])
        n = 0 if j < 0 else int(b[j])
        num = m + n + carry
        carry = num / 2
        res.append(num % 2)
        i -= 1
        j -= 1
    return res[::-1]


if __name__ == '__main__':
    a = '1010'
    b = '1011'
    print add2(a, b)
