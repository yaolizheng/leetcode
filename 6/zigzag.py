def zigzag(s, row):
    rv = [''] * row
    index = 0
    for x in s:
        rv[index] += x
        if index == row - 1:
            next = -1
        if index == 0:
            next = 1
        index += next
    return ''.join(rv)


if __name__ == '__main__':
    s = 'PAYPALISHIRING'
    row = 3
    print zigzag(s, row)
