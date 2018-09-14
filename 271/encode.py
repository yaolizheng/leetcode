def encode(strings):
    res = ''
    for x in strings:
        res += str(len(x)) + '/' + x
    return res


def decode(string):
    i = 0
    res = []
    while i < len(string):
        pos = string.find('/', i)
        print pos
        _len = int(string[i: pos])
        res.append(string[pos + 1: pos + 1 + _len])
        print res
        i = pos + 1 + _len
    return res


if __name__ == '__main__':
    s = ['fs', '2feds', 'fsa2/fd', 'qq8d']
    print s
    en = encode(s)
    print en
    print decode(en)
