from tree import TreeNode


def same_tree(root1, root2):
    if not root1 or not root2:
        return root1 == root2
    return root1.value == root2.value and same_tree(root1.left, root2.left) and same_tree(root1.right, root2.right)


if __name__ == '__main__':
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    print same_tree(root1, root2)
