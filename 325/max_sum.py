def max_sum(nums, k):
    m = dict()
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i - 1]
        m[nums[i]] = i
    res = 0
    for key in m:
        if key == k:
            res = max(res, m[key] + 1)
        else:
            if (key - k) in m:
                res = max(res, m[key] - m[key - k] + 1)
    return res


if __name__ == '__main__':
    nums = [1, 0, -1]
    k = -1
    print max_sum(nums, k)
