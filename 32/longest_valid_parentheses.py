def longest_valid_parentheses(s):
    stack = list()
    stack.append(-1)
    max_length = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])
    return max_length


if __name__ == '__main__':
    s = ')()())'
    print longest_valid_parentheses(s)
