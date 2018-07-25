import heapq


def partition(l):
    x = l[-1]
    p = 0
    for i in range(len(l) - 1):
        if l[i] < x:
            l[i], l[p] = l[p], l[i]
            p += 1
    l[p], l[-1] = l[-1], l[p]
    return p


def kth(l, k):
    l = list(set(l))
    p = partition(l)
    if p == k - 1:
        return l[p]
    elif p < k - 1:
        return kth(l[p + 1:], k - 1 - p)
    else:
        return kth(l[:p], k)


def kth2(l, k):
    l = list(set(l))
    k = len(l) - k + 1
    heap = []
    for x in l:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)
    return heapq.heappop(heap)


if __name__ == '__main__':
    l = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print kth2(l, k)
