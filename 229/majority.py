def majority(l):
    c1 = c2 = None
    n1 = n2 = 0
    for x in l:
        if x == c1:
            n1 += 1
        elif x == c2:
            n2 += 1
        elif n1 == 0:
            c1 = x
            n1 = 1
        elif n2 == 0:
            c2 = x
            n2 = 1
        else:
            n1 -= 1
            n2 -= 1
    return [n for n in [c1, c2] if l.count(n) > len(l) / 3]


if __name__ == '__main__':
    l = [1, 1, 1, 3, 3, 2, 2, 2]
    print majority(l)
