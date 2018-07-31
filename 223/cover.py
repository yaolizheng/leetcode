def cover(A, B, C, D, E, F, G, H):
    a1 = [A, B]
    a2 = [C, D]
    b1 = [E, F]
    b2 = [G, H]
    temp = 0
    if a1[0] > b2[0] or a2[0] < b1[0] or a1[1] > b2[1] or a2[1] < b1[1]:
        pass
    else:
        temp = abs(max(a1[0], b1[0]) - min(a2[0], b2[0])) * abs(max(a1[1], b1[1]) - min(a2[1], b2[1]))
    return (a2[0] - a1[0]) * (a2[1] - a1[1]) + (b2[0] - b1[0]) * (b2[1] - b1[1]) - temp


if __name__ == '__main__':
    A = -3
    B = 0
    C = 3
    D = 4
    E = 0
    F = -1
    G = 9
    H = 2
    print cover(A, B, C, D, E, F, G, H)
