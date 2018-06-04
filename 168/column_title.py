def column_title(n):
    res = ''
    while n > 0:
        n -= 1
        res = chr(65 + n % 26) + res
        n = n / 26
    return res


if __name__ == '__main__':
    n = 701
    print column_title(n)
