def position(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) / 2
        if target < nums[mid]:
            r = mid - 1
        elif target > nums[mid]:
            l = mid + 1
        else:
            return mid
    return l


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 2
    print position(nums, target)
