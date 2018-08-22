from tree import TreeNode


def subtree(root):
    if not root:
        return True
    l = subtree(root.left)
    r = subtree(root.right)
    if l is False or r is False:
        return False
    if root.left and root.value != root.left.value:
        return False
    if root.right and root.value != root.right.value:
        return False
    subtree.count += 1
    return True


def print_tree(root):
    if root is None:
        return
    print root.value
    print_tree(root.left)
    print_tree(root.right)


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(5)
    subtree.count = 0
    subtree(root)
    print subtree.count
