def diff(s, t):
    res = 0
    for x in s:
        res ^= ord(x)
    for x in t:
        res ^= ord(x)
    return chr(res)


if __name__ == '__main__':
    s = "abcd"
    t = "abcde"
    print diff(s, t)
