class sum_range:

    def __init__(self, m):
        row = len(m)
        col = len(m[0])
        self.m = m
        self.dp = [[0] * (col + 1) for x in range(row + 1)]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                self.dp[i][j] = self.dp[i - 1][j] + self.dp[i][j - 1] - self.dp[i - 1][j - 1] + m[i - 1][j - 1]

    def update(self, x, y, v):
        diff = v - self.m[x][y]
        for i in range(1, len(self.m) + 1):
            for j in range(1, len(self.m[0]) + 1):
                if i > x and j > y:
                    self.dp[i][j] += diff
        self.m[x][y] = v

    def sum(self, x, y, a, b):
        return self.dp[a + 1][b + 1] - self.dp[x][b + 1] - self.dp[a + 1][y] + self.dp[x][y]


if __name__ == '__main__':
    m = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    test = sum_range(m)
    print test.sum(2, 1, 4, 3)
    test.update(3, 2, 2)
    print test.sum(2, 1, 4, 3)
