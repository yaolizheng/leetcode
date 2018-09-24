def move_zero(l):
    last_non_zero = 0
    for i in range(len(l)):
        if l[i] != 0:
            l[i], l[last_non_zero] = l[last_non_zero], l[i]
            last_non_zero += 1
    return l


if __name__ == '__main__':
    l = [0, 1, 0, 3, 12]
    print move_zero(l)
