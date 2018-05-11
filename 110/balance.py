from tree import TreeNode


def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def is_balanced(root):
    if not root:
        return True
    left = max_depth(root.left)
    right = max_depth(root.right)
    return (abs(left - right) <= 1) and is_balanced(root.left) and is_balanced(root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)
    print is_balanced(root)
