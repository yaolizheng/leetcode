def palindrome_pairs(w):
    result = []
    mapping = dict()
    l = set()
    for i in range(len(w)):
        mapping[w[i]] = i
        l.add(len(w[i]))
    for i in range(len(w)):
        x = w[i]
        if x[::-1] in mapping and i != mapping[x[::-1]]:
            result.append([i, mapping[x[::-1]]])
        else:
            for _l in l:
                if _l < len(x):
                    if is_palindrome(x, 0, len(x) - _l - 1) and x[len(x) - _l:][::-1] in mapping:
                        result.append([i, mapping[x[len(x) - _l:][::-1]]])
                    elif is_palindrome(x, _l, len(x) - 1) and x[:_l][::-1] in mapping:
                        result.append([i, mapping[x:[_l][::-1]]])
    return result


def is_palindrome(x, s, e):
    while s < e:
        if x[s] != x[e]:
            return False
        s += 1
        e -= 1
    return True


if __name__ == '__main__':
    w = ["abcd", "dcba", "lls", "s", "sssll"]
    print palindrome_pairs(w)
