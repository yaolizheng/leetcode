def guess_num(n):
    l = 1
    r = n
    if guess(n) == 0:
        return n
    while l <= r:
        mid = (l + r) / 2
        rv = guess(mid)
        if rv > 0:
            r = mid - 1
        elif rv < 0:
            l = mid + 1
        else:
            return mid


def guess(n, target=6):
    if n > target:
        return 1
    elif n < target:
        return -1
    else:
        return 0


if __name__ == '__main__':
    print guess_num(10)
