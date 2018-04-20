def helper(c, t, temp, result, i):
    if sum(temp) == t:
        result.append(temp)
        return
    elif sum(temp) > t:
        return
    for index in range(i, len(c)):
        helper(c, t, temp + [c[index]], result, index)


def combination_sum(c, t):
    result = list()
    temp = list()
    helper(c, t, temp, result, 0)
    return result


if __name__ == '__main__':
    c = [2, 3, 6, 7]
    t = 7
    print combination_sum(c, t)
