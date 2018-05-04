def merge_sort(nums1, nums2, m, n):
    l = len(nums1) - 1
    i = m - 1
    j = n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[l] = nums1[i]
            i -= 1
        else:
            nums1[l] = nums2[j]
            j -= 1
        l -= 1
    while j >= 0:
        nums1[l] = nums2[j]
        j -= 1
        l -= 1
    return nums1


if __name__ == '__main__':
    nums1 = [7, 8, 9, 0, 0, 0, 0]
    nums2 = [1, 2, 5, 6]
    m = 3
    n = 4
    print merge_sort(nums1, nums2, m, n)
