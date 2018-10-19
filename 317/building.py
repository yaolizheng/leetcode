import sys


def building(m):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    _sum = m
    val = 0
    res = sys.maxint
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 1:
                dis = m
                queue = list()
                queue.append((i, j))
                while queue:
                    x, y = queue.pop(0)
                    for d in dirs:
                        a = x + d[0]
                        b = y + d[1]
                        if a >= 0 and a < len(m) and b >= 0 and b < len(m[0]) and m[a][b] == val:
                            dis[a][b] = dis[x][y] + 1
                            _sum[a][b] += dis[a][b] - 1
                            queue.append((a, b))
                            res = min(res, _sum[a][b])
                val -= 1
    return res if res != sys.maxint else -1


if __name__ == '__main__':
    m = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
    print building(m)
