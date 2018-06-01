def peak(l):
    i = 0
    j = len(l) - 1
    while i < j:
        mid = (i + j) / 2
        if l[mid] < l[mid + 1]:
            i = mid + 1
        else:
            j = mid
    return i


if __name__ == '__main__':
    l = [1, 2, 1, 3, 5, 6, 4]
    print peak(l)
