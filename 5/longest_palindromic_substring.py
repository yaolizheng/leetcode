def helper(s, i, j):
    length = 0
    while i >= 0 and j < len(s):
        if s[i] == s[j]:
            length = j - i + 1
            i -= 1
            j += 1
        else:
            break
    return length


def longest_palindromic_substring(s):
    maxlen = 0
    start = 0
    for i in range(len(s) - 1):
        l1 = helper(s, i, i)
        l2 = helper(s, i, i + 1)
        if l1 > maxlen:
            maxlen = l1
            start = i - l1 / 2
        if l2 > maxlen:
            maxlen = l2
            start = i - (l2 - 1) / 2
    return s[start: start + maxlen]


def longest_palindromic_substring2(s):
    l = len(s)
    table = [[False] * (l) for i in range(l)]
    maxlen = 0
    start = 0
    for i in range(l):
        table[i][i] = True
        maxlen = 1
        start = i
    for i in range(l - 1):
        if s[i] == s[i + 1]:
            table[i][i + 1] = True
            maxlen = 2
            start = i
    k = 3
    while k <= l:
        i = 0
        while i < (l - k + 1):
            j = i + k - 1
            if s[i] == s[j] and table[i + 1][j - 1]:
                table[i][j] = True
                if k > maxlen:
                    maxlen = k
                    start = i
            i += 1
        k += 1
    return s[start: start + maxlen]

if __name__ == '__main__':
    s = 'babbad'
    print longest_palindromic_substring2(s)
