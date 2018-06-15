def happy_num(n):
    num = set()
    while True:
        if n == 1:
            return True
        sum = 0
        while n > 0:
            sum += (n % 10) * (n % 10)
            n = n / 10
        n = sum
        if n in num:
            return True
        num.add(n)
    return False


if __name__ == '__main__':
    n = 19
    print happy_num(n)
