def largest_num(l):
    l = map(str, l)
    l.sort(cmp=lambda x, y: cmp(y + x, x + y))
    res = ''.join(l)
    return res if res[0] == '0' else res


if __name__ == '__main__':
    l = [3, 30, 34, 5, 9]
    print largest_num(l)
