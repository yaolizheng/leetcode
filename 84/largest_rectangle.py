def largest_rectangle(heights):
    res = 0
    stack = []
    heights.append(0)
    for i in range(len(heights)):
        h = heights[i]
        while len(stack) > 0 and heights[stack[-1]] >= h:
            prev_i = stack.pop()
            prev_h = heights[prev_i]
            length = i - stack[-1] - 1 if len(stack) > 0 else i
            if length * prev_h > res:
                res = length * prev_h
        stack.append(i)
    return res


if __name__ == '__main__':
    heights = [3, 1, 3, 2, 2]
    print largest_rectangle(heights)
