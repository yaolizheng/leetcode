import math


def helper(n, temp, result):
    if len(temp) == n:
        result.append(temp)
    else:
        for x in range(1, n + 1):
            if x not in temp:
                helper(n, temp + [x], result)


def kth_permutations(n, k):
    temp = list()
    result = list()
    helper(n, temp, result)
    return result[k - 1]


def kth_permutations2(n, k):
    l = list(range(1, n + 1))
    ans = []
    k = k - 1
    while k > 0:
        q, r = k / math.factorial(n - 1), k % math.factorial(n - 1)
        ans.append(l[q])
        l.pop(q)
        k = r
        n -= 1
    ans += l
    return ans


if __name__ == '__main__':
    n = 4
    k = 9
    print kth_permutations2(n, k)
