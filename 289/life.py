def life(t):
    dx = [0, 1, 0, -1, 1, 1, -1, -1]
    dy = [1, 0, -1, 0, 1, -1, -1, 1]
    for i in range(len(t)):
        for j in range(len(t[0])):
            count = 0
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if x >= 0 and x < len(t) and y >= 0 and y < len(t[0]) and (t[x][y] == 1 or t[x][y] == 2):
                    count += 1
            if t[i][j] == 1 and (count < 2 or count > 3):
                t[i][j] = 2
            elif t[i][j] == 0 and count == 3:
                t[i][j] = 3
    for i in range(len(t)):
        for j in range(len(t[0])):
            t[i][j] = t[i][j] % 2
    return t


if __name__ == '__main__':
    t = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    print life(t)
