def can_win(s):
    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1] and s[i] == '+':
            if not can_win(s[:i] + '--' + s[i + 2:]):
                return True
    return False


if __name__ == '__main__':
    s = '+++++'
    print can_win(s)
