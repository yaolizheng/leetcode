from tree import TreeNode


def flip_tree(root):
    if not root:
        return root
    if not root.left and not root.right:
        return root
    res = flip_tree(root.left)
    root.left.left = root.right
    root.left.right = root
    root.left = None
    root.right = None
    return res


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root.value
    inorder(root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    inorder(flip_tree(root))
