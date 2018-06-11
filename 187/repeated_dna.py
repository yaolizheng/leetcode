def repeated_dna(s):
    h = set()
    res = []
    if len(s) < 10:
        return None
    for i in range(0, len(s) - 10):
        dna = s[i: i + 10]
        if dna in h:
            res.append(dna)
        h.add(dna)
    return res


if __name__ == '__main__':
    s = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
    print repeated_dna(s)
