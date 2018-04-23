def helper(l, temp, result, used):
    if len(temp) == len(l) and temp not in result:
        result.append(temp)
    else:
        for i in range(len(l)):
            if used[i] is False:
                used[i] = True
                helper(l, temp + [l[i]], result, used)
                used[i] = False


def permutations2(l):
    temp = list()
    result = list()
    used = [False] * len(l)
    helper(l, temp, result, used)
    return result


if __name__ == '__main__':
    l = [1, 1, 2]
    print permutations2(l)
