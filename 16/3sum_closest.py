import sys


def three_sum_closest(s, target):
    s.sort()
    min = sys.maxint
    for i in range(len(s) - 2):
        num = s[i]
        l = i + 1
        r = len(s) - 1
        while l < r:
            c = num + s[l] + s[r]
            if c > target:
                r -= 1
            else:
                l += 1
            if abs(c - target) < min:
                min = c
    return c


if __name__ == '__main__':
    l = [-1, 2, 1, -4]
    target = 1
    print three_sum_closest(l, target)
