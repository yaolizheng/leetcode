def min_rotated_array(s):
    i = 0
    j = len(s) - 1
    while i < j:
        mid = (i + j) / 2
        if mid == i or s[mid - 1] > s[mid]:
            return s[mid]
        elif mid == j or s[mid] > s[mid + 1]:
            return s[mid + 1]
        elif s[mid] > s[j]:
            i = mid + 1
        else:
            j = mid - 1


if __name__ == '__main__':
    s = [6, 0, 1, 2, 3, 4, 5]
    print min_rotated_array(s)
