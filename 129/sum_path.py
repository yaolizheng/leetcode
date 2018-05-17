from tree import TreeNode


def helper(root, val):
    if not root:
        return 0
    val = val * 10 + root.value
    if root.left is None and root.right is None:
        return val
    return helper(root.left, val) + helper(root.right, val)


def sum_path(root):
    return helper(root, 0)


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    print sum_path(root)
