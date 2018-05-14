from tree import TreeNode


def path_sum(root, num):
    if not root:
        return False
    if not root.left and not root.right and num == root.value:
        return True
    return path_sum(root.left, num - root.value) or path_sum(root.right, num - root.value)


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    num = 22
    print path_sum(root, num)
