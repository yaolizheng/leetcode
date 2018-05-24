def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a = a % b
        a, b = b, a
    return a


def max_point(l):
    res = 0
    for i in range(len(l)):
        mapping = {}
        cur_max = 0
        overlapping = 0
        for j in range(i + 1, len(l)):
            if l[i] == l[j]:
                overlapping += 1
            else:
                a = abs(l[j][0] - l[i][0])
                b = abs(l[j][1] - l[i][1])
                _gcd = gcd(a, b)
                slope = (a / _gcd, b / _gcd) if _gcd != 0 else (a, b)
                if slope not in mapping:
                    mapping[slope] = 0
                mapping[slope] += 1
                cur_max = max(cur_max, mapping[slope])
        res = max(res, cur_max + overlapping + 1)
        mapping = {}
    return res


if __name__ == '__main__':
    l = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    print max_point(l)
