def helper(fr, t, res):
    dist = 'ZZZ'
    index = -1
    for i in range(len(t)):
        if t[i][0] == fr:
            if t[i][1] < dist:
                dist = t[i][1]
                index = i
    if index == -1:
        return
    res.append(t[index][1])
    del t[index]
    return helper(dist, t, res)


def tickets(t):
    res = ['JFK']
    helper('JFK', t, res)
    return res


if __name__ == '__main__':
    t = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    print tickets(t)
