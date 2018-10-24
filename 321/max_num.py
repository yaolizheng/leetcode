def max_num(nums1, nums2, k):
    m = len(nums1)
    n = len(nums2)
    res = []
    for i in range(max(0, k - n), min(m, k) + 1):
        res = max(res, merge(_max(nums1, i), _max(nums2, k - i)))
    return res


def _max(n, i):
    res = []
    drop = len(n) - i
    for x in n:
        while drop and res and x > res[-1]:
            del res[-1]
            drop -= 1
        res.append(x)
    return res


def merge(m, n):
    i = 0
    j = 0
    res = []
    while i < len(m) or j < len(n):
        a = m[i] if i < len(m) else -1
        b = n[j] if j < len(n) else -1
        if a > b:
            res.append(a)
            i += 1
        else:
            res.append(b)
            j += 1
    return res


if __name__ == '__main__':
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5
    print max_num(nums1, nums2, k)
