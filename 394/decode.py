def decode(x):
    i = 0
    res = ''
    while i < len(x) and x[i] != ']':
        if x[i].isalpha():
            res += x[i]
            i += 1
        else:
            count = 0
            while x[i].isdigit():
                count = count * 10 + int(x[i])
                i += 1
            tmp = decode(x[i + 1:])
            for _ in range(count):
                res += tmp
            i += len(tmp) + 2
    return res


if __name__ == '__main__':
    x = '2[abc]3[cd]ef'
    print decode(x)
