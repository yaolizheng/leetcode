def max_prod(s):
    max_ends_here = 1
    min_ends_here = 1
    max_so_far = 1
    for x in s:
        if x > 0:
            max_ends_here = max_ends_here * x
            min_ends_here = min(min_ends_here * x, 1)
        elif x == 0:
            max_ends_here = 1
            min_ends_here = 1
        else:
            temp = max_ends_here
            max_ends_here = max(min_ends_here * x, 1)
            min_ends_here = temp * x
        if max_ends_here > max_so_far:
            max_so_far = max_ends_here
    return max_so_far


if __name__ == '__main__':
    s = [2, 3, -2, 4]
    print max_prod(s)
