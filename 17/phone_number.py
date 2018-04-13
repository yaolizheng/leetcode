def phone_num(s, tmp, result):
    if len(s) == 0:
        result.append(tmp)
        return
    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', 9: 'wxyz'}
    for x in mapping[s[0]]:
        phone_num(s[1:], tmp + [x], result)


if __name__ == '__main__':
    s = '23'
    tmp = []
    result = []
    phone_num(s, tmp, result)
    print result
