def count(n):
    tmp = list()
    res = list()
    for i in range(len(n) - 1, -1, -1):
        left = 0
        right = len(tmp)
        while left < right:
            mid = (left + right) / 2
            if n[i] > tmp[mid]:
                left = mid + 1
            else:
                right = mid
        res.append(right)
        tmp.insert(right, n[i])
    return res


if __name__ == '__main__':
    n = [5, 2, 6, 1]
    print count(n)
