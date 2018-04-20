def valid_soduku(table):
    row = len(table)
    col = len(table[0])
    row_used = [[False for x in range(col)] for x in range(row)]
    col_used = [[False for x in range(col)] for x in range(row)]
    sub_used = [[False for x in range(col)] for x in range(row)]
    for i in range(row):
        for j in range(col):
            num = int(table[i][j]) - 1
            if num != -1:
                if row_used[i][num] or col_used[j][num] or sub_used[i / 3 * 3 + j / 3][num]:
                    return False
                row_used[i][num] = col_used[j][num] = sub_used[i / 3 * 3 + j / 3][num] = True
    return True


if __name__ == '__main__':
    table = ['530070000', '600195000', '098000060', '800060003',
             '400803001', '700020006', '060000280', '000419005',
             '000080079']
    print valid_soduku(table)
