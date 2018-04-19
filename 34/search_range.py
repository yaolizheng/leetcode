def find_first(nums, target):
    l = 0
    r = len(nums) - 1
    find = False
    while l <= r:
        mid = (l + r) / 2
        if target > nums[mid]:
            l = mid + 1
        elif target <= nums[mid]:
            if target == nums[mid]:
                find = True
            r = mid - 1
    return l if find else -1


def find_last(nums, target):
    l = 0
    r = len(nums) - 1
    find = False
    while l <= r:
        mid = (l + r) / 2
        if target >= nums[mid]:
            if target == nums[mid]:
                find = True
            l = mid + 1
        elif target < nums[mid]:
            r = mid - 1
    return r if find else -1


def search_range(nums, target):
    return [find_first(nums, target), find_last(nums, target)]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 10
    print search_range(nums, target)
