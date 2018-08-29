from tree import TreeNode


def helper(root, temp, res):
    if not root.left and not root.right:
        res.append(temp + [root.value])
    else:
        if root.left:
            helper(root.left, temp + [root.value], res)
        if root.right:
            helper(root.right, temp + [root.value], res)


def path(root):
    temp = []
    res = []
    helper(root, temp, res)
    return res


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(8)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    print path(root)
