def atoi(num):
    num = num.strip()
    i = 0
    sign = 1
    if num[i] == '+':
        i += 1
    elif num[i] == '-':
        sign = -1
        i += 1
    rv = 0
    max = 2147483647
    min = -2147483648
    while i < len(num):
        try:
            rv = rv * 10 + int(num[i])
        except:
            pass
        i += 1
    rv = rv * sign
    if rv > max:
        return max
    if rv < min:
        return min
    return rv

if __name__ == '__main__':
    num = "       -2147dafsd483649abc"
    print atoi(num)
