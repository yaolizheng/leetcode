import re


def valid_palindrome(s):
    if len(s) == 0:
        return True
    pattern = re.compile('[\W]+')
    s = pattern.sub('', s).lower()
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panamab"
    print valid_palindrome(s)
