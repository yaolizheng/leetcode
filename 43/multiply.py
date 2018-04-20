def multiply(a, b):
    res = [0] * (len(a) + len(b))
    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):
            m = i + j
            n = i + j + 1
            num = int(a[i]) * int(b[j]) + res[n]
            res[n] = num % 10
            res[m] += num / 10
    return int(''.join(map(str, res)))


if __name__ == '__main__':
    a = "123"
    b = "456"
    print multiply(a, b)
