def find_parents(p, n):
    if p[n] == n:
        return n
    return find_parents(p, p[n])


def valid_graph(n, e):
    if len(e) != n - 1:
        return False
    p = dict()
    for i in range(n):
        p[i] = i
    for edge in e:
        a = edge[0]
        b = edge[1]
        a_p = find_parents(p, a)
        b_p = find_parents(p, b)
        if a_p == b_p:
            return False
        p[b] = a_p
    return True


if __name__ == '__main__':
    n = 5
    e = [[0, 1], [0, 2], [1, 2], [1, 4]]
    print valid_graph(n, e)
