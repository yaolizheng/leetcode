def summary_range(l):
    start = end = l[0]
    res = []
    for i in range(1, len(l)):
        if l[i] != l[i - 1] + 1:
            if start == end:
                res.append([start])
            else:
                res.append([start, end])
            start = end = l[i]
        else:
            end = l[i]
    if start == l[-1]:
        res.append([l[-1]])
    else:
        res.append([start, l[-1]])
    return res


if __name__ == '__main__':
    l = [0, 2, 3, 4, 6, 8, 9]
    print summary_range(l)
