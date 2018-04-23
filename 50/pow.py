def pow(s, p):
    is_nag = False
    if p < 0:
        is_nag = True
        p = -p
    ans = 1
    temp = s
    while p > 0:
        if p % 2:
            ans = ans * temp
        temp = temp * temp
        p = p / 2
    return 1 / ans if is_nag else ans


if __name__ == '__main__':
    s = 2.0000
    p = -2
    print pow(s, p)
