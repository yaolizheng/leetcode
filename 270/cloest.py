from tree import TreeNode


def closest(root, t):
    res = root.value
    while root:
        if abs(res - t) >= abs(root.value - t):
            res = root.value
        if t > root.value:
            root = root.right
        else:
            root = root.left
    return res


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(30)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(29)
    root.right.right = TreeNode(100)
    v = 7
    print closest(root, v)
