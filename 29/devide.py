def devide(dividend, divisor):
    res = 0
    while dividend >= divisor:
        temp = divisor
        i = 1
        while dividend >= temp:
            dividend -= temp
            res += i
            temp << 1
            i << 1
    return res


if __name__ == '__main__':
    print devide(10, 3)
