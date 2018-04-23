def group(l):
    res = {}
    for x in l:
        temp = [0] * 26
        for c in x:
            temp[ord(c) - ord('a')] += 1
        temp = tuple(temp)
        if temp not in res:
            res[temp] = list()
        res[temp].append(x)
    return res.values()


if __name__ == '__main__':
    l = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print group(l)
