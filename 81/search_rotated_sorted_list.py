def search_rotated_sorted_list(nums, t):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) / 2
        if nums[mid] == t:
            return True
        if nums[l] == nums[mid]:
            l += 1
        elif nums[l] < nums[mid]:
            if t < nums[mid] and t >= nums[l]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if t > nums[mid] and t <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return False


if __name__ == '__main__':
    nums = [2, 5, 6, 0, 0, 1, 2]
    t = 5
    print search_rotated_sorted_list(nums, t)
