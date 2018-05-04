def gray_code(n):
    if n == 1:
        return ['0', '1']
    l1 = gray_code(n - 1)
    l2 = reversed(l1)
    return ['0' + x for x in l1] + ['1' + x for x in l2]


if __name__ == '__main__':
    n = 4
    print gray_code(n)
