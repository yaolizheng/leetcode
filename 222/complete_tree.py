from tree import TreeNode


def complete_tree(root):
    if not root:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    if lh == rh:
        return 2 ** lh + complete_tree(root.right)
    else:
        return 2 ** rh + complete_tree(root.left)


def height(root):
    h = 0
    while root:
        root = root.left
        h += 1
    return h


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    print complete_tree(root)
