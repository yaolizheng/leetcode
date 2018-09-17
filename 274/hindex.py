def hindex(l):
    l = sorted(l)[::-1]
    print l
    for i in range(len(l)):
        if i >= l[i]:
            return i
    return len(l)


if __name__ == '__main__':
    l = [3, 0, 6, 1, 5]
    print hindex(l)
