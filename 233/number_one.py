def number_one(n):
    i = 1
    rv = 0
    while i <= n:
        devider = i * 10
        rv += n / devider * i + min(max(n % devider - i + 1, 0), i)
        i *= 10
    return rv


if __name__ == '__main__':
    n = 13
    print number_one(n)
