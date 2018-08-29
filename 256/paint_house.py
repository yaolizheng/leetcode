def paint_house(n):
    res = n
    for i in range(2, len(n)):
        res[i][0] += min(res[i - 1][1], res[i - 1][2])
        res[i][1] += min(res[i - 1][2], res[i - 1][0])
        res[i][2] += min(res[i - 1][0], res[i - 1][1])
    return min(res[-1][0], res[-1][1], res[-1][2])


if __name__ == '__main__':
    cost = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    print paint_house(cost)
