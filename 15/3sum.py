def ThreeSum(s):
    s.sort()
    result = []
    for i in range(len(s) - 2):
        num = s[i]
        l = i + 1
        r = len(s) - 1
        while l < r:
            sum = num + s[l] + s[r]
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else:
                if [num, s[l], s[r]] not in result:
                    result.append([num, s[l], s[r]])
                l += 1
                r -= 1
    return result


if __name__ == '__main__':
    s = [-1, 0, 1, 2, -1, -4]
    print ThreeSum(s)
