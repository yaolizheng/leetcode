from tree import TreeNode


def lca(root, a, b):
    if not root or root.value == a or root.value == b:
        return root
    l = lca(root.left, a, b)
    r = lca(root.right, a, b)
    if l and r:
        return root
    return l if r is None else r


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    print lca(root, 4, 5).value
