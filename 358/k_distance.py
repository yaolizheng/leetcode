import heapq


def k_distance(s, k):
    mapping = dict()
    heap = []
    l = len(s)
    for x in s:
        if x not in mapping:
            mapping[x] = 0
        mapping[x] += 1
    for key in mapping:
        heapq.heappush(heap, [mapping[key], key])
    res = ''
    while len(heap) > 0:
        i = min(k, l)
        tmp = []
        for _ in range(i):
            if len(heap) == 0:
                return ''
            next = heapq.heappop(heap)
            res += next[1]
            next[0] -= 1
            if next[0] > 0:
                tmp.append(next)
        for x in tmp:
            heapq.heappush(heap, x)
    return res


if __name__ == '__main__':
    s = 'aabbcc'
    k = 4
    print k_distance(s, k)
