def remove_dup(s):
    if len(s) == 0:
        return 0
    i = 0
    count = 0
    for j in range(0, len(s)):
        if s[i] != s[j]:
            i += 1
            s[i] = s[j]
            count = 0
        else:
            count += 1
            if count < 2:
                i += 1
    return i + 1


if __name__ == '__main__':
    s = [1, 1, 1, 2, 2, 3]
    s = [0,0,1,1,1,1,2,3,3]
    print remove_dup(s)
