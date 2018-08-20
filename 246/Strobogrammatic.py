def IsStrobogrammatic(n):
    i = 0
    j = len(n) - 1
    while i <= j:
        if n[i] == n[j]:
            if n[i] not in ['1', '0', '8']:
                return False
        else:
            if n[i] != '6' or n[j] != '9' and (n[i] != '9' or n[j] != '6'):
                return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    n = '6108019'
    print IsStrobogrammatic(n)
