def is_pow_two(n):
    return n > 0 and (n & (n - 1) == 0)


if __name__ == '__main__':
    n = 1024
    print is_pow_two(n)
