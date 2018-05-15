import sys


def helper(tri, level, sum):
    if level == len(tri):
        if sum < helper.min:
            helper.min = sum
        return
    for i in tri[level]:
        helper(tri, level + 1, sum + i)


def min_path_triangle(tri):
    helper.min = sys.maxint
    helper(tri, 0, 0)
    return helper.min


def min_path_triangle2(tri):
    row = len(tri)
    col = len(tri[-1])
    dp = [0] * col
    for i in range(col):
        dp[i] = tri[-1][i]
    for i in range(row - 2, -1, -1):
        for j in range(len(tri[i])):
            dp[j] = tri[i][j] + min(dp[j], dp[j + 1])
    return dp[0]


if __name__ == '__main__':
    tri = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print min_path_triangle2(tri)
