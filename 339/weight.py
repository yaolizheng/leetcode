def helper(l, level):
    result = 0
    if type(l) is int:
        return l * level
    else:
        for x in l:
            if type(x) is list:
                result += helper(x, level + 1)
            else:
                result += x * level
    return result


def weight(l):
    return helper(l, 1)


if __name__ == '__main__':
    l = [[1, 1], 2, [1, 1]]
    print weight(l)
