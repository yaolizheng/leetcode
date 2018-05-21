def single_int(l):
    return (3 * sum(set(l)) - sum(l)) / 2


if __name__ == '__main__':
    l = [0, 1, 0, 1, 0, 1, 99]
    print single_int(l)
