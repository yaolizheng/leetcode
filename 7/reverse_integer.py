def reverse_integer(num):
    sign = 1
    if num < 0:
        sign = -1
        num = -num
    rv = 0
    while num > 0:
        rv = rv * 10 + num % 10
        num = num / 10
    return rv * sign


if __name__ == '__main__':
    num = -123
    print reverse_integer(num)
