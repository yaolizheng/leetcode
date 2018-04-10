def median(l1, l2):
    m = len(l1)
    n = len(l2)
    half = (m + n + 1) / 2
    i = 0
    j = m
    while i <= j:
        mid1 = (i + j) / 2
        mid2 = half - mid1
        if mid1 > 0 and l1[mid1 - 1] > l2[mid2]:
            j = mid1 - 1
        elif mid1 < m and l1[mid1] < l2[mid2 - 1]:
            i = mid1 + 1
        else:
            max_l = 0
            if mid1 == 0:
                max_l = l2[mid2 - 1]
            elif mid2 == 0:
                max_l = l1[mid1 - 1]
            else:
                max_l = max(l1[mid1 - 1], l2[mid2 - 1])
            if (m + n) % 2:
                return max_l
            min_r = 0
            if mid1 == m:
                min_r = l2[mid2]
            elif mid2 == n:
                min_r = l1[mid1]
            else:
                min_r = min(l1[mid1], l2[mid2])
            return (min_r + max_l) / 2.0


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    print median(nums1, nums2)
