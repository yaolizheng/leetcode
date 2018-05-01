import collections


def min_window(l, t):
    map = dict(collections.Counter(t))
    print map
    start = end = 0
    res = ""
    while end < len(l):
        if l[end] in map:
            map[l[end]] -= 1
        while all(x <= 0 for x in map.values()):
            candidate = l[start: end + 1]
            if len(res) == 0 or len(candidate) < len(res):
                res = candidate
            if l[start] in map:
                map[l[start]] += 1
            start += 1
        end += 1
    return res


if __name__ == '__main__':
    l = "ADOBECODEBANC"
    t = "ABC"
    print min_window(l, t)
