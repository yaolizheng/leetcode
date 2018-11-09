def is_power_of_four(n):
    return n > 0 and not (n & (n - 1)) and n & 0x55555555 == n


if __name__ == '__main__':
    n = 18
    print is_power_of_four(n)
