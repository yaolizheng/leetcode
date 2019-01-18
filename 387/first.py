def first(l):
    count = dict()
    for x in l:
        if x not in count:
            count[x] = 0
        count[x] += 1
    for i in range(len(l)):
        if count[l[i]] == 1:
            return i
    return -1


if __name__ == '__main__':
    l = 'loveleetcode'
    print first(l)
