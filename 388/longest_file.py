def longest_file(s):
    depth = dict()
    n = len(s)
    res = -1
    level = 0
    depth[0] = 0
    i = 0
    while i < n:
        start = i
        while i < n and s[i] not in ['\n', '\t']:
            i += 1
        if i >= n or s[i] == '\n':
            name = s[start:i]
            print name
            if '.' in name:
                res = max(res, depth[level] + len(name))
            else:
                level += 1
                depth[level] = depth[level - 1] + len(name) + 1
            level = 0
        else:
            level += 1
        i += 1
    return res


if __name__ == '__main__':
    s = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
    print longest_file(s)
