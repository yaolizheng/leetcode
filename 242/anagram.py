def is_anagram(s, t):
    counter = dict()
    if len(s) != len(t):
        return False
    for x in s:
        if x not in counter:
            counter[x] = 0
        counter[x] += 1
    for x in t:
        if x not in counter:
            return False
        counter[x] -= 1
        if counter[x] < 0:
            return False
    return all(v == 0 for v in counter.values())


if __name__ == '__main__':
    s = "anagram"
    t = "nagarbm"
    print is_anagram(s, t)
