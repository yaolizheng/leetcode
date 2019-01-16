def canConstruct(n, m):
    count = dict()
    for x in m:
        if x not in count:
            count[x] = 0
        count[x] += 1
    for x in n:
        if x not in count:
            return False
        count[x] -= 1
        if count[x] < 0:
            return False
    return True


if __name__ == '__main__':
    n = 'aaa'
    m = 'aab'
    print canConstruct(n, m)
