def helper(num, m, n, jump, res, visited, l):
    if l >= m:
        res += 1
    l += 1
    if l > n:
        return res
    visited[num] = True
    for i in range(1, 10):
        if visited[i] is False and (jump[num][i] == 0 or visited[jump[num][i]]):
            res = helper(i, m, n, jump, res, visited, l)
    visited[num] = False
    return res


def unlock(m, n):
    jump = [[0] * 10 for x in range(10)]
    visited = [False] * 10
    jump[1][3] = jump[3][1] = 2
    jump[1][7] = jump[7][1] = 4
    jump[1][9] = jump[9][1] = 5
    jump[2][8] = jump[8][2] = 5
    jump[3][7] = jump[7][3] = 5
    jump[3][9] = jump[9][3] = 6
    jump[4][6] = jump[6][4] = 5
    jump[7][9] = jump[9][7] = 8
    res = 0
    res += helper(1, m, n, jump, 0, visited, 1) * 4
    res += helper(2, m, n, jump, 0, visited, 1) * 4
    res += helper(5, m, n, jump, 0, visited, 1)
    return res


if __name__ == '__main__':
    m = 1
    n = 1
    print unlock(m, n)
