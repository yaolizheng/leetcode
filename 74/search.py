def search_matrix(m, target):
    row = len(m)
    col = len(m[0])
    l = 0
    r = row * col - 1
    while l <= r:
        mid = (l + r) / 2
        num = m[mid / col][mid % col]
        if num == target:
            return True
        elif num > target:
            l = mid + 1
        else:
            r = mid - 1
    return False


if __name__ == '__main__':
    m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target = 51
    print search_matrix(m, target)
