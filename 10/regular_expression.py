def regular_expression(s, p, i, j):
    if j == len(p):
        return i == len(s)
    is_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
    if j + 2 <= len(p) and p[j + 1] == '*':
        return regular_expression(s, p, i, j + 2) or (is_match and regular_expression(s, p, i + 1, j))
    else:
        return is_match and regular_expression(s, p, i + 1, j + 1)


def is_match(s, p):
    return regular_expression(s, p, 0, 0)


if __name__ == '__main__':
    print is_match('aa', 'a')
    print is_match('aa', 'aa')
    print is_match('aaa', 'aa')
    print is_match('aa', 'a*')
    print is_match('ab', '.*')
    print is_match('aab', 'c*a*b*')
