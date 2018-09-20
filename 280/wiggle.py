def wiggle(l):
    l.sort()
    print l
    for i in range(2, len(l), 2):
        l[i], l[i - 1] = l[i - 1], l[i]
    return l


def wiggle2(l):
    for i in range(1, len(l)):
        if (i % 2 == 0 and l[i] > l[i - 1]) or (i % 2 == 1 and l[i] < l[i - 1]):
            l[i], l[i - 1] = l[i - 1], l[i]
    return l


if __name__ == '__main__':
    l = [3, 5, 2, 1, 6, 4]
    print wiggle2(l)
