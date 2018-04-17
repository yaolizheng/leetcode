def remove(s, val):
    j = len(s) - 1
    for i in range(len(s) - 1, -1, -1):
        if s[i] == val:
            s[i] = s[j]
            j -= 1
    return j + 1


if __name__ == '__main__':
    s = [3, 2, 2, 3]
    print remove(s, 3)
