def longest_substring(s, k):
    mapping = dict()
    left = 0
    res = 0
    for i in range(len(s)):
        if s[i] not in mapping:
            mapping[s[i]] = 0
        mapping[s[i]] += 1
        while len(mapping) > k:
            mapping[s[left]] -= 1
            if mapping[s[left]] == 0:
                del mapping[s[left]]
                left += 1
        res = max(res, i - left + 1)
    return res


if __name__ == '__main__':
    s = 'eceba'
    k = 2
    print longest_substring(s, k)
