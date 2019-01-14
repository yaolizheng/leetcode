def kth(m, k):
    l = m[0][0]
    r = m[-1][-1]
    while l < r:
        mid = (l + r) / 2
        cnt = 0
        for i in range(len(m)):
            cnt += len([x for x in m[i] if x <= mid])
        if cnt < k:
            l = mid + 1
        else:
            r = mid
    return l


if __name__ == '__main__':
    m = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print kth(m, k)
