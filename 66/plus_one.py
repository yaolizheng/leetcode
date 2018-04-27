def plus_one(num):
    carry = 0
    result = []
    for i in range(len(num) - 1, -1, -1):
        if i == len(num) - 1:
            n = num[i] + carry + 1
        else:
            n = num[i] + carry
        if n == 10:
            carry = 1
            n = 0
        else:
            carry = 0
        result.append(n)
        print result
    if carry == 1:
        result.append(1)
    return result[::-1]


if __name__ == '__main__':
    num = [9, 9, 9, 9]
    print plus_one(num)
