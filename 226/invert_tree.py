from tree import TreeNode


def preorder(root):
    if not root:
        return
    print root.value
    preorder(root.left)
    preorder(root.right)


def invert_tree(root):
    if not root:
        return None
    left = invert_tree(root.left)
    right = invert_tree(root.right)
    root.left = right
    root.right = left
    return root


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    preorder(invert_tree(root))
