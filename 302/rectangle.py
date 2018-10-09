def helper(m, i, j, low, high, herizon, search_low):
    while i < j:
        mid = (i + j) / 2
        black = False
        for x in range(low, high):
            temp = m[x][mid] if herizon else m[mid][x]
            if temp == '1':
                black = True
                break
        if black == search_low:
            j = mid
        else:
            i = mid + 1
    return j


def rectangle(m, x, y):
    row = len(m)
    col = len(m[0])
    left = helper(m, 0, y, 0, row, True, True)
    right = helper(m, y + 1, col, 0, row, True, False)
    top = helper(m, 0, x, left, right, False, True)
    down = helper(m, x + 1, row, left, right, False, False)
    return (right - left) * (down - top)


if __name__ == '__main__':
    m = ["0010", "0110", "0100"]
    print rectangle(m, 0, 2)
