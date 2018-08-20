def helper(l, h, n, length):
    if len(n) >= length:
        if len(n) != length or (len(n) != 1 and n[0] == '0'):
            return
        if length == len(l) and int(n) < int(l) or (length == len(h) and int(n) > int(h)):
            return
        helper.size += 1
    helper(l, h, '0' + n + '0', length)
    helper(l, h, '1' + n + '1', length)
    helper(l, h, '8' + n + '8', length)
    helper(l, h, '6' + n + '9', length)
    helper(l, h, '9' + n + '6', length)


def strobogrammatic(l, h):
    helper.size = 0
    for i in range(len(l), len(h) + 1):
        helper(l, h, '', i)
        helper(l, h, '0', i)
        helper(l, h, '1', i)
        helper(l, h, '8', i)
    return helper.size


if __name__ == '__main__':
    l = '50'
    h = '100'
    print strobogrammatic(l, h)
