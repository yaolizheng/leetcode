def helper(w1, w2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if w1[m - 1] == w2[n - 1]:
        return helper(w1, w2, m - 1, n - 1)
    return 1 + min(helper(w1, w2, m - 1, n), helper(w1, w2, m, n - 1), helper(w1, w2, m - 1, n - 1))


def edit_distance(w1, w2):
    return helper(w1, w2, len(w1), len(w2))


def edit_distance2(w1, w2):
    l1 = len(w1)
    l2 = len(w2)
    table = [[0] * (l2 + 1) for i in range(l1 + 1)]
    for i in range(l1 + 1):
        for j in range(l2 + 1):
            if i == 0:
                table[i][j] = j
            elif j == 0:
                table[i][j] = i
            elif w1[i - 1] == w2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i - 1][j - 1], table[i - 1][j], table[i][j - 1])
    return table[l1][l2]


if __name__ == '__main__':
    w1 = 'horse'
    w2 = 'ros'
    print edit_distance2(w1, w2)
