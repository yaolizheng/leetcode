def matrix(a, b):
    res = [[0] * len(b) for x in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != 0:
                for k in range(len(b[0])):
                    if b[j][k] != 0:
                        res[i][j] += a[i][j] * b[j][k]
    return res


if __name__ == '__main__':
    a = [[1, 0, 0], [-1, 0, 3]]
    b = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
    print matrix(a, b)
