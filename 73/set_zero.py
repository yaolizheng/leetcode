def set_zero(m):
    r = len(m)
    c = len(m[0])
    for i in range(r):
        for j in range(c):
            if m[i][j] == 0:
                m[0][j] = 's'
                m[i][0] = 's'
    for i in range(r):
        if m[i][0] == 's':
            for j in range(c):
                if m[i][j] != 's':
                    m[i][j] = 0
    for j in range(c):
        if m[0][j] == 's':
            for i in range(r):
                m[i][j] = 0
    return m


if __name__ == '__main__':
    m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    m = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    print set_zero(m)
