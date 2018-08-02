def compare(c):
    if c in ['*', '/']:
        return 2
    elif c in ['+', '-']:
        return 1
    else:
        return 0


def cal(a, b, o):
    a = int(a)
    b = int(b)
    if o == '+':
        return a + b
    elif o == '-':
        return a - b
    elif o == '*':
        return a * b
    elif o == '/':
        return a / b


def evaluate(s):
    value = []
    op = []
    for x in s:
        if x == ' ':
            continue
        elif x == '(':
            op.append(x)
        elif x == ')':
            while len(op) > 0 and op[-1] != '(':
                a = value.pop()
                b = value.pop()
                o = op.pop()
                value.append(cal(b, a, o))
            op.pop()
        elif x.isdigit():
            value.append(x)
        elif x in ['+', '-', '*', '/']:
            while len(op) > 0 and compare(op[-1]) >= compare(x):
                a = value.pop()
                b = value.pop()
                o = op.pop()
                value.append(cal(b, a, o))
            op.append(x)
    while len(op) > 0:
        a = value.pop()
        b = value.pop()
        o = op.pop()
        value.append(cal(b, a, o))
    return value[0]


if __name__ == '__main__':
    s = " 3+5 / 2 "
    print evaluate(s)
