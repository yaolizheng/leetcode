def helper(board, row, col, i, j, word, index):
    if i == row or j == col or i < 0 or j < 0:
        return False
    if index == len(word):
        return True
    if board[i][j] == word[index]:
        temp = board[i][j]
        board[i][j] = ''
        res = helper(board, row, col, i + 1, j, word, index + 1) or (
            helper(board, row, col, i, j + 1, word, index + 1)) or (
            helper(board, row, col, i - 1, j, word, index + 1)) or (
            helper(board, row, col, i, j - 1, word, index + 1))
        board[i][j] = temp
        return res
    return False


def word_search(board, word):
    row = len(board)
    col = len(board[0])
    for i in range(row):
        for j in range(col):
            if board[i][j] == word[0]:
                if helper(board, row, col, i, j, word, 0):
                    return True
    return False


if __name__ == '__main__':
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    word = 'ABCCED'
    print word_search(board, word)
