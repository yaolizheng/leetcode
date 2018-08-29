def add_digits(n):
    return (n - 1) % 9 + 1


if __name__ == '__main__':
    n = 38
    print add_digits(n)
