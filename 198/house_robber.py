def house_robber(l):
    n = len(l)
    if n == 1:
        return l[0]
    if n == 2:
        return max(l[0], l[1])
    if n == 3:
        return max(l[0] + l[2], l[1])
    table = [0] * n
    table[0] = l[0]
    table[1] = max(l[0], l[1])
    table[2] = max(l[0] + l[2], l[1])
    for i in range(3, n):
        table[i] = max(l[i] + table[i - 2], table[i - 1])
    return table[-1]


if __name__ == '__main__':
    l = [2, 7, 9, 3, 1]
    print house_robber(l)
