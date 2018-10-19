def remove_dup(l):
    mapping = dict()
    visited = dict()
    res = '0'
    for x in l:
        if x not in mapping:
            mapping[x] = 0
        mapping[x] += 1
        if x not in visited:
            visited[x] = False
    for x in l:
        mapping[x] -= 1
        if visited[x] is True:
            continue
        while x < res[-1] and mapping[res[-1]]:
            visited[res[-1]] = False
            res = res[:-1]
        res += x
        visited[x] = True
    return res[1:]


if __name__ == '__main__':
    l = 'cbacdcbc'
    print remove_dup(l)
