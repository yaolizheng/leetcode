def pascal(n):
    if n == 1:
        return [[1]]
    res = pascal(n - 1)
    last = pascal(n - 1)[-1]
    next = [1]
    prev = 1
    for i in range(1, len(last)):
        next.append(prev + last[i])
        prev = last[i]
    next.append(1)
    res.append(next)
    return res


def pascal2(n):
    res = []
    for i in range(n):
        row = [0] * (i + 1)
        row[0] = 1
        row[-1] = 1
        for j in range(1, len(row) - 1):
            row[j] = res[i - 1][j - 1] + res[i - 1][j]
        res.append(row)
    return res


if __name__ == '__main__':
    n = 5
    print pascal2(n)
