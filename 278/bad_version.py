def is_bad_version(n):
    pass


def find_bad_version(n):
    l = 0
    r = len(n) - 1
    while l < r:
        mid = (l + r) / 2
        if is_bad_version(mid + 1):
            r = mid
        else:
            l = mid + 1
    return r + 1


if __name__ == '__main__':
    pass
