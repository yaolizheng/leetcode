def ndigit(n):
    _len = 1
    start = 1
    count = 9
    while n > count * _len:
        n -= count * _len
        _len += 1
        count *= 10
        start *= 10
    start += (n - 1) / _len
    return str(start)[(n - 1) % _len]


if __name__ == '__main__':
    n = 11
    print ndigit(n)
