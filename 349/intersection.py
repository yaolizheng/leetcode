def intersection(a, b):
    return list(set([x for x in a if x in b]))


if __name__ == '__main__':
    a = [1, 2, 2, 1]
    b = [2, 2]
    print intersection(a, b)
