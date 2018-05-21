def helper(s, d, start, temp, res):
    if start == len(s):
        res.append(temp)
        return
    for i in range(start, len(s)):
        if s[start: i + 1] in d:
            helper(s, d, i + 1, temp + [s[start: i + 1]], res)


def word_break(s, d):
    res = []
    helper(s, d, 0, [], res)
    return res


if __name__ == '__main__':
    s = 'catsanddog'
    d = ["cat", "cats", "and", "sand", "dog"]
    print word_break(s, d)
