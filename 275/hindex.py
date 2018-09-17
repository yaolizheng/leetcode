def hindex(l):
    left = 0
    n = len(l)
    right = n - 1
    while left <= right:
        mid = (left + right) / 2
        if l[mid] == n - mid:
            return n - mid
        elif l[mid] > n - mid:
            right = mid - 1
        else:
            left = left + 1
    return n - left


if __name__ == '__main__':
    l = [0, 1, 3, 5, 6]
    print hindex(l)
