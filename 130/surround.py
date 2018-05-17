def surround(s):
    m = len(s)
    n = len(s[0])
    board = []
    board += [(0, i) for i in range(n - 1)]
    board += [(i, n - 1) for i in range(m - 1)]
    board += [(m - 1, i) for i in range(1, n)]
    board += [(i, 0) for i in range(1, m)]
    while len(board) > 0:
        (i, j) = board.pop()
        if 0 <= i < m and 0 <= j < n and s[i][j] == 'O':
            s[i][j] = 'S'
            board += [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    for i in range(m):
        for j in range(n):
            if s[i][j] == 'S':
                s[i][j] = 'O'
            elif s[i][j] == 'O':
                s[i][j] = 'X'
    return s


if __name__ == '__main__':
    s = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
    print surround(s)
