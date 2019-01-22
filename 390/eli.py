def eli(n):
    l = range(1, n + 1)
    l2r = True
    while len(l) > 1:
        if l2r:
            res = []
            i = 1
            while i < len(l):
                res.append(l[i])
                i += 2
            l = res
            l2r = False
        else:
            res = []
            i = len(l) - 2
            while i >= 0:
                res.insert(0, l[i])
                i -= 2
            l = res
            l2r = True
    return l[0]


if __name__ == '__main__':
    n = 9
    print eli(n)
