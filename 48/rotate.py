def rotate(s):
    # s = s[::-1]
    s = [x[::-1] for x in s]
    r = len(s)
    l = len(s[0])
    for i in range(r):
        for j in range(i + 1, l):
            temp = s[i][j]
            s[i][j] = s[j][i]
            s[j][i] = temp
    return s


if __name__ == '__main__':
    s = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print rotate(s)
