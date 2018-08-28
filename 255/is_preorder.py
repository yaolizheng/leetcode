import sys


def is_preorder(l):
    low = -sys.maxint - 1
    stack = []
    for i in range(len(l)):
        if l[i] < low:
            return False
        while len(stack) > 0 and l[i] > stack[-1]:
            low = stack.pop()
        stack.append(l[i])
    return True


if __name__ == '__main__':
    l = [5, 6, 2]
    print is_preorder(l)
