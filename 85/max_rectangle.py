def max_rec(m):
    res = 0
    for line in m:
        line.append(0)
    heights = [0] * (len(m[0]) + 1)
    for i in range(len(m)):
        stack = []
        for j in range(len(m[0])):
            if m[i][j] == 1:
                heights[j] += 1
            else:
                heights[j] = 0
            h = heights[j]
            while len(stack) > 0 and heights[stack[-1]] >= h:
                prev_i = stack.pop()
                prev_h = heights[prev_i]
                length = j - stack[-1] - 1 if len(stack) > 0 else j
                if length * prev_h > res:
                    res = length * prev_h
            stack.append(j)
    return res


if __name__ == '__main__':
    m = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]
    print max_rec(m)
