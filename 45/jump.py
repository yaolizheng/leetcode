def jump_2(l):
    start = 0
    end = 0
    n = len(l)
    step = 0
    while end < n - 1:
        step += 1
        maxend = end + 1
        for i in range(start, end + 1):
            if i + l[i] >= n:
                return step
            maxend = max(maxend, i + l[i])
        start = end + 1
        end = maxend
    return step


if __name__ == '__main__':
    l = [2, 3, 1, 1, 4]
    print jump_2(l)
