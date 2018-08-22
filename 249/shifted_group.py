def get_diff(x):
    if len(x) == 1:
        return [0]
    diff = list()
    for i in range(1, len(x)):
        diff.append((ord(x[i]) - ord(x[i - 1])) % 26)
    return diff


def shifted_group(l):
    cache = dict()
    for x in l:
        diff = str(get_diff(x))
        if diff not in cache:
            cache[diff] = list()
        cache[diff].append(x)
    return cache.values()


if __name__ == '__main__':
    l = ["acd", "dfg", "wyz", "yab", "mop", "bdfh", "a", "x", "moqs"]
    print shifted_group(l)
