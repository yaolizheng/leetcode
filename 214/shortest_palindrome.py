def LPS(n):
    lps = [0] * len(n)
    lps[0] = 0
    l = 0
    i = 1
    while i < len(n):
        if n[i] == n[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l != 0:
                l = lps[l - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def shortest_palin(n):
    index = LPS(n + '&' + n[::-1])[-1]
    return n[index:][::-1] + n


if __name__ == '__main__':
    n = 'aacecaaa'
    print shortest_palin(n)
