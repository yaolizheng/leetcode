def simplify_path(path):
    stack = list()
    for x in path.split('/'):
        if x == '' or x == '.':
            continue
        elif x == '..':
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(x)
    return '/' + '/'.join(stack)


if __name__ == '__main__':
    path = '/../'
    print simplify_path(path)
