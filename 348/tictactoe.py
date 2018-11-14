class TicTacToe:

    def __init__(self, n):
        self.n = n
        self.row = [0] * n
        self.col = [0] * n
        self.d1 = 0
        self.d2 = 0

    def move(self, row, col, player):
        p = -1 if player == 1 else 1
        self.row[row] += p
        self.col[col] += p
        if row == col:
            self.d1 += p
        elif row == self.n - col + 1:
            self.d2 += p
        return player if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.d1) == self.n or abs(self.d2) == self.n else 0


if __name__ == '__main__':
    test = TicTacToe(3)
    print test.move(0, 0, 1)
    print test.move(0, 2, 2)
    print test.move(2, 2, 1)
    print test.move(1, 1, 2)
    print test.move(2, 0, 1)
    print test.move(1, 0, 2)
    print test.move(2, 1, 1)
