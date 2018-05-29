def min_rotated_array(s):
    for i in range(1, len(s)):
        if s[i] < s[i - 1]:
            return s[i]
    return s[-1]


if __name__ == '__main__':
    s = [2, 2, 2, 2, 2, 2, 2, 2, 0]
    print min_rotated_array(s)
