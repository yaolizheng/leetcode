def window(l, k):
    q = []
    for i in range(k):
        while len(q) and l[i] >= q[-1]:
            q.pop()
        q.append(i)
    res = []
    for i in range(k, len(l)):
        res.append(l[q[0]])
        if len(q) and q[0] <= (i - k):
            del q[0]
        while len(q) and l[i] >= q[-1]:
            q.pop()
        q.append(i)
    res.append(l[q[0]])
    return res


if __name__ == '__main__':
    l = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print window(l, k)
