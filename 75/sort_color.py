def sort_color(l):
    m = n = 0
    for i in range(len(l)):
        temp = l[i]
        l[i] = 2
        if temp < 2:
            l[m] = 1
            m += 1
        if temp < 1:
            l[n] = 0
            n += 1
    return l


if __name__ == '__main__':
    l = [2, 0, 2, 1, 1, 0]
    print sort_color(l)
