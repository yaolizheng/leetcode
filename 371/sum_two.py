def sum_two(a, b):
    if b == 0:
        return a
    _sum = a ^ b
    carry = (a & b) << 1
    return sum_two(_sum, carry)


if __name__ == '__main__':
    a = 1
    b = 5
    print sum_two(a, b)
