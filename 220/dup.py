def duplicate(l, k, t):
    b = dict()
    w = t + 1
    for i in range(len(l)):
        x = l[i] / w
        if x in b:
            return True
        if x - 1 in b and abs(l[i] - b[x - 1]) < w:
            return True
        if x + 1 in b and abs(l[i] - b[x + 1]) < w:
            return True
        b[x] = l[i]
        if i >= k:
            del b[l[i - k] / w]
    return False


if __name__ == '__main__':
    l = [1, 5, 9, 1, 5, 9]
    k = 2
    t = 3
    print duplicate(l, k, t)
