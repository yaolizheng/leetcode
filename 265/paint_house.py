def paint_house(n):
    min1 = min2 = -1
    res = n
    for i in range(len(n)):
        last1 = min1
        last2 = min2
        min1 = min2 = -1
        for j in range(len(n[0])):
            if j != last1:
                res[i][j] = res[i][j] if last1 < 0 else res[i][j] + res[i - 1][last1]
            else:
                res[i][j] = res[i][j] if last2 < 0 else res[i][j] + res[i - 1][last2]
            if min1 < 0 or res[i][j] < res[i][min1]:
                min2 = min1
                min1 = j
            elif min2 < 0 or res[i][j] < res[i][min2]:
                min2 = j
    return res[-1][min1]


if __name__ == '__main__':
    cost = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    print paint_house(cost)
