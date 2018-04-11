import sys


def LCP(l):
    min_len = sys.maxint
    rv = ''
    for x in l:
        min_len = min(min_len, len(x))
    for i in range(min_len):
        match = l[0][i]
        for j in range(1, len(l)):
            if l[j][i] != match:
                return rv
        rv += match
    return rv


if __name__ == '__main__':
    l = ['abcd', 'abcdefg', 'abcedf', 'abc']
    print LCP(l)
