def longest_consecutive_sequence(l):
    h = set()
    res = 0
    for i in l:
        h.add(i)
    for i in l:
        if (i - 1) not in h:
            j = i
            while j in h:
                j += 1
            res = max(res, j - i)
    return res


if __name__ == '__main__':
    l = [100, 4, 200, 1, 3, 2, 5, 6]
    print longest_consecutive_sequence(l)
