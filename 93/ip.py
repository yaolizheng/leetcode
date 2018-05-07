def helper(s, index, temp, res):
    if len(temp) == 4 and index < len(s):
        return
    if len(temp) == 4 and index == len(s):
        res.append(temp)
        return
    end = index + 3 if index + 3 <= len(s) else len(s)
    for i in range(index, end):
        if 0 <= int(s[index: i + 1]) <= 255:
            helper(s, i + 1, temp + [int(s[index: i + 1])], res)


def restore_ip(s):
    res = list()
    helper(s, 0, [], res)
    return res


if __name__ == '__main__':
    s = "25525511135"
    print restore_ip(s)
