def two_sum(l, t):
    start = 0
    end = len(l) - 1
    while start < end:
        if l[start] + l[end] < t:
            start += 1
        elif l[start] + l[end] > t:
            end -= 1
        else:
            return [start + 1, end + 1]


if __name__ == '__main__':
    l = [2, 7, 11, 15]
    t = 9
    print two_sum(l, t)
