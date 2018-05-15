def pascal(n):
    row = [1]
    for i in range(1, n):
        row = [x + y for x, y in zip([0] + row, row + [0])]
    return row


if __name__ == '__main__':
    n = 5
    print pascal(n)
