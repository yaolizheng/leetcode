def excel_column(s):
    res = 0
    for i in range(len(s)):
        res = res * 26 + (ord(s[i]) - 64)
    return res


if __name__ == '__main__':
    s = "ZY"
    print excel_column(s)
