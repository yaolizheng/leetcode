def helper(l, temp, result):
    if len(temp) == len(l):
        result.append(temp)
    else:
        for x in l:
            if x not in temp:
                helper(l, temp + [x], result)


def permutations(l):
    temp = list()
    result = list()
    helper(l, temp, result)
    return result


if __name__ == '__main__':
    l = [1, 2, 3]
    print permutations(l)
