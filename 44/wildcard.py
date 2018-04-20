def match(s, p):
    i = 0
    j = 0
    match = 0
    star = -1
    while i < len(s):
        if j < len(p) and (s[i] == p[j] or p[j] == '?'):
            i += 1
            j += 1
        elif j < len(p) and p[j] == '*':
            star = j
            match = i
            j += 1
        elif star != -1:
            j = star + 1
            match += 1
            i = match
        else:
            return False
    while j < len(p) and j == '*':
        j += 1
    return j == len(p)


if __name__ == '__main__':
    s = "aa"
    p = "a"
    print match(s, p)
