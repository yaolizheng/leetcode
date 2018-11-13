import heapq


def k_top(l, k):
    m = dict()
    for x in l:
        if x not in m:
            m[x] = 0
        m[x] += 1
    s = []
    for key in m:
        heapq.heappush(s, (m[key], key))
    return [x[1] for x in heapq.nlargest(k, s)]


if __name__ == '__main__':
    l = [1, 1, 1, 2, 2, 3]
    k = 1
    print k_top(l, k)
