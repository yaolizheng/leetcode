def evaluate(eq, v, query):
    table = dict()
    res = []
    for i in range(len(eq)):
        table[(eq[i][0], eq[i][1])] = v[i]
        table[(eq[i][1], eq[i][0])] = 1.0 / v[i]
    for x in query:
        visited = set()
        tmp = helper(x[0], x[1], table, visited)
        res.append(tmp)
    return res


def helper(s, e, table, visited):
    if (s, e) in table:
        return table[(s, e)]
    for k in table:
        if k[0] != s:
            continue
        if k not in visited:
            visited.add(k)
            tmp = helper(k[1], e, table, visited)
            if tmp > 0:
                return tmp * table[k]
    return -1.0


if __name__ == '__main__':
    eq = [['a', 'b'], ['b', 'c']]
    v = [2.0, 3.0]
    query = [['a', 'c'], ['b', 'a'], ['a', 'e']]
    print evaluate(eq, v, query)
