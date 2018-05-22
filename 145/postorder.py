from tree import TreeNode


def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print root.value


def postorder2(root):
    stack = [root]
    stack2 = []
    while len(stack) > 0:
        root = stack.pop()
        stack2.append(root.value)
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)
    while len(stack2) > 0:
        print stack2.pop()


def postorder3(root):
    stack = []
    while True:
        while root:
            if root.right:
                stack.append(root.right)
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.right and len(stack) > 0 and root.right == stack[-1]:
            stack.pop()
            stack.append(root)
            root = root.right
        else:
            print root.value
            root = None
        if len(stack) <= 0:
            break


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    postorder3(root)
