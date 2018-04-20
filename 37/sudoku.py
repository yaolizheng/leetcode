def is_valid(soduku, i, j, num):
    for x in range(9):
        if soduku[x][j] == num:
            return False
        if soduku[i][x] == num:
            return False
    for row in range(i / 3 * 3, i / 3 * 3 + 3):
        for col in range(j / 3 * 3, j / 3 * 3 + 3):
            if soduku[row][col] == num:
                return False
    return True


def solve(soduku):
    for i in range(len(soduku)):
        for j in range(len(soduku[0])):
            if soduku[i][j] == 0:
                for num in range(10):
                    if is_valid(soduku, i, j, num):
                        soduku[i][j] = num
                        if solve(soduku):
                            return True
                        else:
                            soduku[i][j] = 0
                return False
    return True


if __name__ == '__main__':
    soduku = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    print solve(soduku)
    print soduku
