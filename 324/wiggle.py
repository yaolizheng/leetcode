def wiggle(nums):
    nums.sort()
    print nums
    i = len(nums) / 2
    j = len(nums) - 1
    res = list()
    while i >= 0:
        res.append(nums[i])
        res.append(nums[j])
        i -= 1
        j -= 1
    return res


if __name__ == '__main__':
    nums = [1, 5, 1, 1, 6, 4, 3]
    print wiggle(nums)
