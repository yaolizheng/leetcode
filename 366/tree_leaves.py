from tree import TreeNode


def remove_leaves(root):
    if not root:
        return root
    if not root.left and not root.right:
        remove_leaves.res.append(root.value)
        return None
    root.left = remove_leaves(root.left)
    root.right = remove_leaves(root.right)
    return root


def tree_leaves(root):
    res = []
    while root:
        remove_leaves.res = []
        root = remove_leaves(root)
        res.append(remove_leaves.res)
    return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print tree_leaves(root)
