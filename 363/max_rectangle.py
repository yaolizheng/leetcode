import sys


def max_rectangle(matrix, k):
    m = len(matrix)
    n = len(matrix[0])
    s = [[0] * n for x in range(m)]
    res = -sys.maxint - 1
    for i in range(m):
        for j in range(n):
            t = matrix[i][j]
            if i > 0:
                t += s[i - 1][j]
            if j > 0:
                t += s[i][j - 1]
            if i > 0 and j > 0:
                t -= s[i - 1][j - 1]
            s[i][j] = t
            for x in range(i + 1):
                for y in range(j + 1):
                    tmp = s[i][j]
                    if x > 0:
                        tmp -= s[x - 1][j]
                    if y > 0:
                        tmp -= s[i][y - 1]
                    if x > 0 and y > 0:
                        tmp += s[x - 1][y - 1]
                    if tmp <= k:
                        res = max(res, tmp)
    return res


if __name__ == '__main__':
    matrix = [[1, 0, 1], [0, -2, 3]]
    k = 2
    print max_rectangle(matrix, k)
