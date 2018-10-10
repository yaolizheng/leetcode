def island(m, n, p):
    root = dict()
    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    count = 0
    res = list()
    for x in p:
        if str(x) not in root:
            root[str(x)] = str(x)
            count += 1
        for d in dirs:
            a = x[0] + d[0]
            b = x[1] + d[1]
            if a < 0 or a >= m or b < 0 or b >= n or str([a, b]) not in root:
                continue
            p = find_root(root, str([a, b]))
            q = find_root(root, str(x))
            if p != q:
                root[str(p)] = str(q)
                count -= 1
        res.append(count)
    return res


def find_root(root, id):
    return root[id] if id == root[id] else find_root(root, str(root[id]))


if __name__ == '__main__':
    p = [[0, 0], [0, 1], [1, 2], [2, 1]]
    m = 3
    n = 3
    print island(m, n, p)
