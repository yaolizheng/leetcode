def count_prime(n):
    temp = [True] * (n + 1)
    if n < 2:
        return 0
    temp[0] = temp[1] = False
    for i in range(2, n + 1):
        if temp[i] is True:
            for j in range(2, n / i + 1):
                temp[i * j] = False
    return sum(temp)


if __name__ == '__main__':
    n = 10
    print count_prime(n)
