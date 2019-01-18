def lexi(n):
    res = [0] * n
    cur = 1
    for i in range(n):
        res[i] = cur
        if cur * 10 <= n:
            cur = cur * 10
        else:
            if cur >= n:
                cur = cur / 10
            cur += 1
            while cur % 10 == 0:
                cur = cur / 10
    return res


if __name__ == '__main__':
    n = 50
    print lexi(n)
