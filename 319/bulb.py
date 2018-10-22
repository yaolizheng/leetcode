def bulb(n):
    res = 1
    while res * res <= n:
        res += 1
    return res - 1


if __name__ == '__main__':
    n = 36
    print bulb(n)
