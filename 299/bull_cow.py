def bull_cow(s, g):
    m = [0] * 256
    bull = 0
    cow = 0
    for i in range(len(s)):
        a = int(s[i])
        b = int(g[i])
        if a == b:
            bull += 1
        else:
            if m[a] < 0:
                cow += 1
            m[a] += 1
            if m[b] > 0:
                cow += 1
            m[b] -= 1
    return str(bull) + 'A' + str(cow) + 'B'


if __name__ == '__main__':
    s = "1807"
    g = "7810"
    print bull_cow(s, g)
