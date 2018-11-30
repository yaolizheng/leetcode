def unique_digits(n):
    res = 0
    for i in range(n):
        res += count(i + 1)
    return res


def count(n):
    res = 9
    if n == 1:
        return 10
    for i in range(9, 11 - n - 1, -1):
        res *= i
    return res


if __name__ == '__main__':
    n = 3
    print unique_digits(n)
