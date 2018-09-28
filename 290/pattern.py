def pattern(p, s):
    mapping = dict()
    s = s.split(" ")
    if len(s) != len(p):
        return False
    for i in range(len(s)):
        if p[i] not in mapping:
            mapping[p[i]] = s[i]
        else:
            if mapping[p[i]] != s[i]:
                return False
    return True


if __name__ == '__main__':
    p = "abba"
    s = "dog cat cat fish"
    print pattern(p, s)
