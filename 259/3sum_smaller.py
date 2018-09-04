def sum_smaller(n, t):
    n.sort()
    length = len(n)
    res = 0
    for i in range(length):
        l = i + 1
        r = length - 1
        while l < r:
            s = n[i] + n[l] + n[r]
            if s < t:
                res += r - l
                l += 1
            else:
                r -= 1
    return res


if __name__ == '__main__':
    n = [-2, 0, 1, 3]
    t = 2
    print sum_smaller(n, t)
