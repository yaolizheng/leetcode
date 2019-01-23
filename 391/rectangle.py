def is_rectangle(m):
    s = set()
    min_x = 1000
    max_x = 1
    min_y = 1000
    max_y = 1
    area = 0
    for n in m:
        min_x = min(min_x, n[0])
        max_x = max(max_x, n[2])
        min_y = min(min_y, n[1])
        max_y = max(max_y, n[3])
        area += (n[2] - n[0]) * (n[3] - n[1])
        for x in [(n[0], n[1]), (n[0], n[3]), (n[2], n[3]), (n[2], n[1])]:
            if x not in s:
                s.add(x)
            else:
                s.remove(x)
    if (min_x, min_y) not in s or (min_x, max_y) not in s or (
        max_x, max_y
    ) not in s or (max_x, max_y) not in s or len(s) != 4:
        return False
    return area == (max_x - min_x) * (max_y - min_y)


if __name__ == '__main__':
    m = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]
    print is_rectangle(m)
