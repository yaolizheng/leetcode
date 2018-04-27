def sqrt(num):
    res = num
    while res * res > num:
        res = (res + num / res) / 2
    return res


if __name__ == '__main__':
    num = 4
    print sqrt(num)
