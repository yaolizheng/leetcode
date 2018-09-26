def dup(l):
    i = l[0]
    j = l[0]
    while True:
        i = l[i]
        j = l[l[j]]
        if i == j:
            break
    i = l[0]
    while True:
        i = l[i]
        j = l[j]
        if i == j:
            break
    return i


if __name__ == '__main__':
    l = [1, 3, 4, 2, 2]
    print dup(l)
