def helper(nums, start, temp, res):
    res.append(temp)
    for i in range(start, len(nums)):
        helper(nums, i + 1, temp + [nums[i]], res)


def subsets(nums):
    res = []
    helper(nums, 0, [], res)
    return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    print subsets(nums)
