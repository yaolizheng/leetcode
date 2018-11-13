def is_vowel(c):
    return c in ['a', 'e', 'i', 'o', 'u']


def reverse_vowel(s):
    l = list(s)
    i = 0
    j = len(l) - 1
    left = right = False
    while i < j:
        if is_vowel(l[i]):
            left = True
        else:
            i += 1
        if is_vowel(l[j]):
            right = True
        else:
            j -= 1
        if left and right:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
    return ''.join(l)


if __name__ == '__main__':
    s = 'leetcode'
    print reverse_vowel(s)
