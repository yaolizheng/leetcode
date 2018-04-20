def helper(c, t, temp, result, i):
    if sum(temp) == t:
        result.append(temp)
        return
    elif sum(temp) > t:
        return
    for index in range(i, len(c)):
        if index > i and c[i] == c[i - 1]:
            continue
        helper(c, t, temp + [c[index]], result, index + 1)


def combination_sum_2(c, t):
    result = list()
    temp = list()
    c.sort()
    helper(c, t, temp, result, 0)
    return result


if __name__ == '__main__':
    c = [10, 1, 2, 7, 6, 1, 5]
    t = 8
    print combination_sum_2(c, t)
