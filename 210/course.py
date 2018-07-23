def helper(g, v, visited, result):
    visited.append(v)
    for e in g[v]:
        if e not in visited:
            helper(g, e, visited, result)
    result.insert(0, v)


def topsort(g):
    visited = []
    result = []
    for v in g:
        if v not in visited:
            helper(g, v, visited, result)
    return result


def course(n, c):
    g = dict()
    for i in range(n):
        g[i] = []
    for i, j in c:
        g[j].append(i)
    return topsort(g)


if __name__ == '__main__':
    n = 4
    c = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print course(n, c)
