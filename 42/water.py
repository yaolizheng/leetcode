def trapping_water(n):
    l = 0
    r = len(n) - 1
    max_l = 0
    max_r = 0
    ans = 0
    while l < r:
        if n[l] < n[r]:
            if n[l] > max_l:
                max_l = n[l]
            else:
                ans += max_l - n[l]
            l += 1
        else:
            if n[r] > max_r:
                max_r = n[r]
            else:
                ans += max_r - n[r]
            r -= 1
    return ans


if __name__ == '__main__':
    n = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print trapping_water(n)
