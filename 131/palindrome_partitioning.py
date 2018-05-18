def is_valid(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def helper(s, i, temp, res):
    if i >= len(s):
        res.append(temp)
        return
    for j in range(i, len(s)):
        if is_valid(s, i, j):
            helper(s, j + 1, temp + [s[i:j + 1]], res)


def palindrome_partitioning(s):
    res = []
    helper(s, 0, [], res)
    return res


if __name__ == '__main__':
    s = 'aab'
    print palindrome_partitioning(s)
