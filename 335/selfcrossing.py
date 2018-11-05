def selfcrossing(l):
    for i in range(3, len(l)):
        if l[i] >= l[i - 2] and l[i - 3] >= l[i - 1]:
            return True
        if i >= 4 and l[i - 1] == l[i - 3] and l[i] >= l[i - 2] - l[i - 4]:
            return True
        if i >= 5 and l[i - 2] >= l[i - 4] and l[i - 3] >= l[i - 1] and l[i - 1] >= l[i - 3] - l[i - 5] and l[i] >= l[i - 2] - l[i - 4]:
            return True
    return False


if __name__ == '__main__':
    l = [1, 1, 1, 1]
    print selfcrossing(l)
