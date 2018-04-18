def next_permutation(num):
    length = len(num)
    i = length - 2
    while i >= 0 and num[i + 1] <= num[i]:
        i -= 1
    if i >= 0:
        j = length - 1
        while j > 0 and num[j] <= num[i]:
            j -= 1
        num[j], num[i] = num[i], num[j]
    num[i + 1: length] = reversed(num[i + 1: length])
    return num


if __name__ == '__main__':
    num = [3, 2, 1]
    print next_permutation(num)
