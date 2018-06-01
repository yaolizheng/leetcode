def one_edit(s1, s2):
    m = len(s1)
    n = len(s2)
    if abs(m - n) > 1:
        return False
    i = j = 0
    count = 0
    while i < m and j < n:
        if s1[i] != s2[j]:
            count += 1
            if count > 1:
                return False
            if m > n:
                i += 1
            elif m < n:
                j += 1
            else:
                j += 1
                i += 1
        i += 1
        j += 1
    if i < m or j < n:
        count += 1
    return count == 1


if __name__ == '__main__':
    s1 = 'geeo'
    s2 = 'geek'
    print one_edit(s1, s2)
