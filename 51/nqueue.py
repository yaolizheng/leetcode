def print_table(t):
    for i in range(len(t)):
        print t[i]


def is_valid(nums, n):
    for i in range(n):
        if abs(nums[n] - nums[i]) == n - i or nums[i] == nums[n]:
            return False
    return True


def n_queue(nums, index, res, table):
    if index == len(nums):
        res.append(table)
        return
    for i in range(len(nums)):
        nums[index] = i
        if is_valid(nums, index):
            temp = '.' * len(nums)
            n_queue(nums, index + 1, res, table + [temp[:i] + 'Q' + temp[i + 1:]])


def nqueue(n):
    res = list()
    table = list()
    nums = [-1] * n
    n_queue(nums, 0, res, table)
    return res


if __name__ == '__main__':
    n = 4
    print nqueue(n)
