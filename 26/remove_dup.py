def remove_dup(s):
    if len(s) == 0:
        return 0
    i = 0
    for j in range(0, len(s)):
        if s[i] != s[j]:
            i += 1
            s[i] = s[j]
    return i + 1


if __name__ == '__main__':
    s = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print remove_dup(s)
