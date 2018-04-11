def RtoI(r):
    map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rv = 0
    for i in range(len(r) - 1):
        if r[i + 1] > r[i]:
            rv += -map[r[i]]
        else:
            rv += map[r[i]]
    return rv + map[r[-1]]


if __name__ == '__main__':
    r = 'VIII'
    print RtoI(r)
