from tree import TreeNode


def helper(root1, root2):
    if not root1 or not root2:
        return root1 == root2
    return (root1.value == root2.value) and helper(root1.left, root2.right) and helper(root1.right, root2.left)


def is_symmetric(root):
    return helper(root, root)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(4)
    print is_symmetric(root)
