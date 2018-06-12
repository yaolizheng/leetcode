def hamming_weight(n):
    count = 0
    for i in range(32):
        if n % 2 == 1:
            count += 1
        n >>= 1
    return count


if __name__ == '__main__':
    n = 128
    print hamming_weight(n)
