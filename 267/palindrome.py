from collections import Counter


def palindrome(n):
    c = Counter(n)
    even = ''
    odd = ''
    temp = ''
    used = [False] * len(n)
    for key in c:
        if c[key] % 2 == 0:
            even += key
        else:
            if odd is not None:
                return []
            odd = key
    used = [False] * len(even)
    res = list()
    permutation(even, temp, res, used, odd)
    return res


def permutation(n, temp, res, used, odd):
    if len(temp) == len(n) and temp not in res:
        res.append(temp + odd + temp[::-1])
    else:
        for i in range(len(n)):
            if not used[i]:
                used[i] = True
                permutation(n, temp + n[i], res, used, odd)
                used[i] = False


if __name__ == '__main__':
    n = 'aabbcd'
    print palindrome(n)
