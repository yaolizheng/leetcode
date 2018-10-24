def num_connected(n, e):
    root = list()
    res = n
    for i in range(n):
        root.append(i)
    for v1, v2 in e:
        a = find_root(root, v1)
        b = find_root(root, v2)
        if a != b:
            res -= 1
            root[b] = a
    return res


def find_root(root, v):
    while root[v] != v:
        v = root[v]
    return v


if __name__ == '__main__':
    n = 5
    e = [[0, 1], [1, 2], [3, 4]]
    print num_connected(n, e)
