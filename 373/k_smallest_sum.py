def k_smallest_sum(a, b, k):
    mapping = dict()
    for i in range(min(len(a), k)):
        for j in range(min(len(b), k)):
            _sum = a[i] + b[j]
            if _sum not in mapping:
                mapping[_sum] = list()
            mapping[_sum].append((a[i], b[j]))
    res = []
    for tmp in mapping.values():
        for x in tmp:
            res.append(x)
            if len(res) >= k:
                return res
    return res


if __name__ == '__main__':
    a = [1, 1, 2]
    b = [1, 2, 3]
    k = 22
    print k_smallest_sum(a, b, k)
