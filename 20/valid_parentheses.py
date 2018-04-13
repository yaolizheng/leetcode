def valid_parentheses(s):
    if len(s) == 0:
        return True
    parentheses = {'{': '}', '[': ']', '(': ')'}
    stack = list()
    stack.append(s[0])
    for i in range(1, len(s)):
        if s[i] in parentheses.keys():
            stack.append(s[i])
        elif s[i] in parentheses.values():
            if parentheses[stack.pop()] != s[i]:
                return False
    return len(stack) == 0


if __name__ == '__main__':
    print valid_parentheses('()')
    print valid_parentheses('()[]{}')
    print valid_parentheses('(]')
    print valid_parentheses('([)]')
    print valid_parentheses('{[]}')
