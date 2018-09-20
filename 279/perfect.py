import math
import sys


def perfect(n):
    while n % 4 == 0:
        n = n / 4
    if n % 8 == 7:
        return 4
    i = 0
    while i * i <= n:
        j = math.sqrt(n - i * i)
        if (j * j + i * i) == n:
            r1 = 1 if i != 0 else 0
            r2 = 1 if j != 0 else 0
            return r1 + r2
        i += 1
    return 3


def perfect2(n):
    res = [sys.maxint] * (n + 1)
    res[0] = 0
    for i in range(n + 1):
        j = 0
        while (i + j * j) <= n:
            res[i + j * j] = min(res[i + j * j], res[i] + 1)
            j += 1
    return res


if __name__ == '__main__':
    n = 12
    print perfect(n)
