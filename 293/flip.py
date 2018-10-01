def flip(s):
    res = list()
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1] and s[i] == '+':
            res.append(s[:i] + '--' + s[i + 2:])
    return res


if __name__ == '__main__':
    s = '++++'
    print flip(s)
