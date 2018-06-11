def rotate(l, k):
    k = k % len(l)
    return l[-k:] + l[:len(l) - k]


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print rotate(l, k)
