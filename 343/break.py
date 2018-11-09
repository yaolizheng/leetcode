def num_break(n):
    if n == 2:
        return 1
    if n == 3:
        return 2
    res = 1
    while n > 4:
        res *= 3
        n -= 3
    return res * n


if __name__ == '__main__':
    n = 10
    print num_break(n)
