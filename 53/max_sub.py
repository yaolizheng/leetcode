import sys


def max_subarray(nums):
    max_ending_here = 0
    max_so_far = -sys.maxint - 1
    for x in nums:
        max_ending_here += x
        max_so_far = max(max_so_far, max_ending_here)
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


if __name__ == '__main__':
    nums = [-2, -1, -3]
    print max_subarray(nums)
