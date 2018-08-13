def product(l):
    n = len(l)
    temp = []
    p = 1
    for i in range(0, n):
        temp.append(p)
        p *= l[i]
    p = 1
    for i in range(n - 1, -1, -1):
        temp[i] *= p
        p *= l[i]
    return temp


if __name__ == '__main__':
    l = [1, 2, 3, 4]
    print product(l)
