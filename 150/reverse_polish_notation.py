def evaluate(l):
    stack = []
    for x in l:
        if x in ['+', '-', '*', '/']:
            b = stack.pop()
            a = stack.pop()
            if x == '+':
                stack.append(a + b)
            elif x == '-':
                stack.append(a - b)
            elif x == '*':
                stack.append(a * b)
            else:
                stack.append(int(float(a) / b))
        else:
            stack.append(int(x))
    return stack.pop()


if __name__ == '__main__':
    l = ["2", "1", "+", "3", "*"]
    l = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print evaluate(l)
