import sys


def max_profit(p, k):
    n = len(p)
    profit = [[0] * (n) for x in range(k + 1)]
    for i in range(n):
        profit[0][i] = 0
    for i in range(k + 1):
        profit[i][0] = 0
    for i in range(1, k + 1):
        max_diff = -sys.maxint - 1
        for j in range(1, n):
            max_diff = max(max_diff, profit[i - 1][j - 1] - p[j - 1])
            profit[i][j] = max(profit[i][j - 1], max_diff + p[j])
    return profit[k][n - 1]


if __name__ == '__main__':
    p = [3, 2, 6, 5, 0, 3]
    k = 2
    print max_profit(p, k)
