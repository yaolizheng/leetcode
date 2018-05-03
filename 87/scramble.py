def scramble(s1, s2):
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return True
    counter = dict()
    check = True
    for x in s1:
        if x not in counter:
            counter[x] = 0
        counter[x] += 1
    for x in s2:
        if x not in counter:
            check = False
            break
        counter[x] -= 1
    if check is False or not all(x == 0 for x in counter.values()):
        return False
    for i in range(1, len(s1)):
        if scramble(s1[:i], s2[:i]) and scramble(s1[i:], s2[i:]):
            return True
        if scramble(s1[:i], s2[i:]) and scramble(s1[i:], s2[:i]):
            return True
    return False

if __name__ == '__main__':
    s1 = 'abcde'
    s2 = 'bacde'
    print scramble(s1, s2)
