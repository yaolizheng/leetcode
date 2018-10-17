def ugly_num(n, prime):
    result = [1]
    index = [0] * len(prime)
    while len(result) < n:
        tmp = []
        for i in range(len(prime)):
            tmp.append(result[index[i]] * prime[i])
        _min = min(tmp)
        for i in range(len(tmp)):
            if tmp[i] == _min:
                index[i] += 1
        result.append(_min)
    return result[-1]


if __name__ == '__main__':
    n = 10
    prime = [2, 7, 13, 19]
    print ugly_num(n, prime)
