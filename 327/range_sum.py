import bisect


def range_sum(l, lower, upper):
    res = 0
    sum = 0
    sums = [0]
    for i in range(len(l)):
        sum += l[i]
        res += abs(bisect.bisect_left(sums, sum - upper) - bisect.bisect_right(sums, sum - lower))
        sums.append(sum)
    return res


if __name__ == '__main__':
    l = [-2, 5, -1]
    lower = -2
    upper = 2
    print range_sum(l, lower, upper)
