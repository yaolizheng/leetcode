def comb_sum(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for x in nums:
            if i >= x:
                dp[i] += dp[i - x]
    return dp[-1]


if __name__ == '__main__':
    nums = [4, 1, 2]
    target = 32
    print comb_sum(nums, target)
