def find_skyline(n, l, r):
    if l == r:
        return [[n[l][0], n[l][2]], [n[l][1], 0]]
    mid = (l + r) / 2
    lr = find_skyline(n, l, mid)
    rr = find_skyline(n, mid + 1, r)
    res = merge(lr, rr)
    return res


def merge(s1, s2):
    h1 = h2 = 0
    i = j = 0
    res = []
    h = 0
    while i < len(s1) and j < len(s2):
        if s1[i][0] < s2[j][0]:
            h1 = s1[i][1]
            h = max(h1, h2)
            if len(res) == 0 or h != res[-1][1]:
                res.append([s1[i][0], h])
            i += 1
        else:
            h2 = s2[j][1]
            h = max(h1, h2)
            if len(res) == 0 or h != res[-1][1]:
                res.append([s2[j][0], h])
            j += 1
    while i < len(s1):
        res.append(s1[i])
        i += 1
    while j < len(s2):
        res.append(s2[j])
        j += 1
    return res


def skyline(l):
    return find_skyline(l, 0, len(l) - 1)


if __name__ == '__main__':
    l = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    print skyline(l)
