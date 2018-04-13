def generaet_parentheses(i, j, temp, res):
    if i == 0 and j == 0:
        res.append(temp)
    else:
        if i > 0:
            generaet_parentheses(i - 1, j, temp + ['('], res)
        if j > i:
            generaet_parentheses(i, j - 1, temp + [')'], res)


if __name__ == '__main__':
    res = temp = list()
    n = 3
    generaet_parentheses(n, n, temp, res)
    print res
