def meeting(m):
    row = list()
    col = list()
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 1:
                row.append(i)
                col.append(j)
    col.sort()
    i = 0
    j = len(row) - 1
    res = 0
    while i < j:
        res += row[j] - row[i] + col[j] - col[i]
        i += 1
        j -= 1
    return res


if __name__ == '__main__':
    m = [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
    print meeting(m)
