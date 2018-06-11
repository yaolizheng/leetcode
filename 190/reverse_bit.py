def reverse_bits(n):
    res = 0
    for i in range(32):
        res <<= 1
        res += n % 2
        print res
        n >>= 1
    return res


if __name__ == '__main__':
    n = 43261596
    print reverse_bits(n)
