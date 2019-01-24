def longest(s, k):
    res = 0
    i = 0
    n = len(s)
    while i + k <= n:
        m = [0] * 26
        mask = 0
        index = i
        for j in range(i, n):
            x = ord(s[j]) - ord('a')
            m[x] += 1
            if m[x] >= k:
                mask &= ~ (1 << k)
            else:
                mask |= (1 << k)
            if mask == 0:
                res = max(res, j - i + 1)
                index = j
        i = index + 1
    return res


if __name__ == '__main__':
    s = 'aaabb'
    k = 3
    print longest(s, k)
