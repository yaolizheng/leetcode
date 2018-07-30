def duplicate(l, k):
    t = dict()
    for i in range(len(l)):
        x = l[i]
        if x not in t:
            t[x] = i
        else:
            if i - t[x] <= k:
                return True
            t[x] = i
    return False


if __name__ == '__main__':
    l = [1, 2, 3, 1]
    k = 3
    print duplicate(l, k)
