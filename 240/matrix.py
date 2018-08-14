def matrix(m, k):
    row = 0
    col = len(m[0]) - 1
    while col >= 0 and row < len(m):
        if m[row][col] == k:
            return True
        elif m[row][col] > k:
            col -= 1
        elif m[row][col] < k:
            row += 1
    return False


if __name__ == '__main__':
    m = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    k = 25
    print matrix(m, k)
