def is_ugly(n):
    for i in [2, 3, 5]:
        while n % i == 0:
            n = n / i
    return n == 1


if __name__ == '__main__':
    n = 28
    print is_ugly(n)
