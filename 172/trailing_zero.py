def trailing_zero(n):
    res = 0
    while n != 0:
        n = n / 5
        res += n
    return res


if __name__ == '__main__':
    n = 25
    print trailing_zero(n)
