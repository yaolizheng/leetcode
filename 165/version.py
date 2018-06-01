def version(v1, v2):
    l1 = v1.split('.')
    l2 = v2.split('.')
    m = len(l1)
    n = len(l2)
    if m > n:
        for _ in range(m - n):
            l2.append(0)
    elif m < n:
        for _ in range(n - m):
            l1.append(0)
    for i in range(len(l1)):
        if l1[i] > l2[i]:
            return 1
        elif l1[i] < l2[i]:
            return -1
    return 0


if __name__ == '__main__':
    v1 = "7.5.2.4"
    v2 = "7.5.3"
    print version(v1, v2)
