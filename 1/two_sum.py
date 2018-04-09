def two_sum(nums, target):
    search_list = dict()
    for i in range(len(nums)):
        remain = target - nums[i]
        if remain in search_list:
            return [i, search_list[remain]]
        else:
            search_list[nums[i]] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print two_sum(nums, target)
