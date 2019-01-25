def replace(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + replace(n / 2)
    else:
        return 1 + max(replace(n - 1), replace(n + 1))


if __name__ == '__main__':
    n = 8
    print replace(n)
