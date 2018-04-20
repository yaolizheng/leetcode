def find_first_missing(l):
    length = max(l)
    l = l + [-1] * (length - len(l) + 1)
    for i in range(len(l)):
        while l[i] != -1 and l[i] != i:
            j = l[i]
            l[i], l[j] = l[j], l[i]
    for i in range(1, len(l)):
        if i != l[i]:
            return i
    return len(l)


if __name__ == '__main__':
    l = [1, 2, 0]
    print find_first_missing(l)
