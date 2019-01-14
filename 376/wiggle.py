def max_wiggle(l):
    n = len(l)
    pos = [1] * n
    neg = [1] * n
    for i in range(n):
        for j in range(i):
            if l[i] > l[j]:
                pos[i] = max(pos[i], neg[j] + 1)
            elif l[i] < l[j]:
                neg[i] = max(neg[i], pos[j] + 1)
    return max(pos[-1], neg[-1])


if __name__ == '__main__':
    l = [1, 7, 4, 9, 2, 5]
    print max_wiggle(l)
