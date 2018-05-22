from tree import TreeNode


def preorder(root):
    if not root:
        return
    print root.value
    preorder(root.left)
    preorder(root.right)


def preorder2(root):
    stack = [root]
    while len(stack) > 0:
        root = stack.pop()
        print root.value
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    preorder2(root)
