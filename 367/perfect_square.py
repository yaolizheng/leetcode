def is_perfect_square(n):
    l = 0
    r = n
    while l <= r:
        mid = (l + r) / 2
        t = mid * mid
        if t == n:
            return True
        elif n > t:
            l = mid + 1
        else:
            r = mid - 1
    return False


if __name__ == '__main__':
    n = 149
    print is_perfect_square(n)
