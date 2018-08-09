from tree import TreeNode


def lca(root, a, b):
    if not root:
        return None
    if root.value > a and root.value > b:
        return lca(root.left, a, b)
    if root.value < a and root.value < b:
        return lca(root.right, a, b)
    return root.value


if __name__ == '__main__':
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    print lca(root, 3, 5)
