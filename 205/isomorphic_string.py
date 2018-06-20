def isomorphic_string(s, t):
    visited = set()
    mapping = dict()
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] not in mapping:
            if t[i] in visited:
                return False
            visited.add(t[i])
            mapping[s[i]] = t[i]
        else:
            if mapping[s[i]] != t[i]:
                return False
    return True


if __name__ == '__main__':
    s = 'egk'
    t = 'add'
    print isomorphic_string(s, t)
