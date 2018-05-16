def best_time(l):
    max = 0
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            max += l[i] - l[i - 1]
    return max


if __name__ == '__main__':
    l = [7, 1, 5, 3, 6, 4]
    # l = [7, 6, 4, 3, 1]
    print best_time(l)
