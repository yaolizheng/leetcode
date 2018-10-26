def power_of_three(n):
    while n > 0 and n % 3 == 0:
        n = n / 3
    return n == 1


if __name__ == '__main__':
    n = 28
    print power_of_three(n)
