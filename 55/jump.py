def jump(j):
    end = 0
    start = 0
    n = len(j)
    while end < n - 1:
        max_end = end + 1
        for i in range(start, end + 1):
            if i + j[i] >= n - 1:
                return True
            max_end = max(max_end, i + j[i])
        start = end + 1
        end = max_end
    return False


if __name__ == '__main__':
    j = [3, 2, 1, 0, 4]
    print jump(j)
