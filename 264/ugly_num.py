def nth_ugly(n):
    l1 = l2 = l3 = 0
    res = [1]
    while len(res) < n:
        m1 = res[l1] * 2
        m2 = res[l2] * 3
        m3 = res[l3] * 5
        m = min(m1, m2, m3)
        if m == m1:
            l1 += 1
        elif m == m2:
            l2 += 1
        else:
            l3 += 1
        res.append(m)
    return res[-1]


if __name__ == '__main__':
    n = 10
    print nth_ugly(n)
