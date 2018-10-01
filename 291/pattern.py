def helper(p, s, p_index, s_index, m):
    if p_index == len(p) and s_index == len(s):
        return True
    if p_index == len(p) or s_index == len(s):
        return False
    p_curr = p[p_index]
    for i in range(s_index, len(s)):
        s_curr = s[s_index: i + 1]
        if p_curr in m and m[p_curr] == s_curr:
            if helper(p, s, p_index + 1, i + 1, m):
                return True
        elif p_curr not in m:
            if s_curr not in m.values():
                m[p_curr] = s_curr
                if helper(p, s, p_index + 1, i + 1, m):
                    return True
                del m[p_curr]
    return False


def pattern(p, s):
    m = dict()
    return helper(p, s, 0, 0, m)


if __name__ == '__main__':
    p = "aaaa"
    s = "asdasdasdasde"
    print pattern(p, s)
