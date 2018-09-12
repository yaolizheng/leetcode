def alien_dict(l):
    graph = dict()
    for i in range(len(l) - 1, 0, -1):
        cur = l[i]
        prev = l[i - 1]
        _len = min(len(cur), len(prev))
        for j in range(_len):
            if cur[j] != prev[j]:
                if cur[j] not in graph:
                    graph[cur[j]] = set()
                graph[cur[j]].add(prev[j])
    print graph
    return top_sort(graph)


def helper(g, v, visited, res):
    visited.add(v)
    if v in g:
        for _v in g[v]:
            if _v not in visited:
                helper(g, _v, visited, res)
    res.append(v)


def top_sort(g):
    res = []
    visited = set()
    for v in g:
        if v not in visited:
            helper(g, v, visited, res)
    return res


if __name__ == '__main__':
    l = ["wrt", "wrf", "er", "ett", "rftt"]
    print alien_dict(l)
