def max_area(height):
    l = 0
    r = len(height) - 1
    max_a = 0
    while l < r:
        max_a = max(max_a, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_a


if __name__ == '__main__':
    pass
