def climb(n):
    a = 1
    b = 1
    if n == 0:
        return a
    if n == 1:
        return b
    for i in range(2, n + 1):
        f = a + b
        a = b
        b = f
    return f


if __name__ == '__main__':
    n = 3
    print climb(3)
