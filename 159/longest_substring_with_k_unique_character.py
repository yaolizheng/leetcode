def is_valid(l, k):
    count = 0
    for x in l:
        if l[x] > 0:
            count += 1
    return count <= k


def longest_substring_with_k_unique_character(s, k):
    max_len = 0
    i = 0
    j = 0
    count = dict()
    uniq = 0
    for x in s:
        if x not in count:
            count[x] = 0
            uniq += 1
        count[x] += 1
    if uniq < k:
        return -1
    count = dict()
    while j < len(s):
        if s[j] not in count:
            count[s[j]] = 0
        count[s[j]] += 1
        while not is_valid(count, k):
            count[s[i]] -= 1
            i += 1
            print count
        if (j - i + 1) > max_len:
            max_len = j - i + 1
        j += 1
    return max_len


if __name__ == '__main__':
    k = 3
    s = 'aabbcc'
    print longest_substring_with_k_unique_character(s, k)
