def ThreeSum(s, n):
    s.sort()
    result = []
    for i in range(len(s) - 2):
        num = s[i]
        l = i + 1
        r = len(s) - 1
        while l < r:
            sum = num + s[l] + s[r] + n
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else:
                if [n, num, s[l], s[r]] not in result:
                    result.append([n, num, s[l], s[r]])
                l += 1
                r -= 1
    return result


def FourSum(s):
    rv = []
    for i in range(len(s) - 3):
        num = s[i]
        rv += ThreeSum(s[i + 1:], num)
    return rv


if __name__ == '__main__':
    s = [1, 0, -1, 0, -2, 2]
    print FourSum(s)
