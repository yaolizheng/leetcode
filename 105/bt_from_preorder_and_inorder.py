from tree import TreeNode


def bt_from_preorder_and_inorder(preorder, inorder):
    if len(preorder) <= 0:
        return None
    root = TreeNode(preorder[0])
    index = inorder.index(preorder[0])
    root.left = bt_from_preorder_and_inorder(preorder[1: 1 + index], inorder[0: index])
    root.right = bt_from_preorder_and_inorder(preorder[1 + index:], inorder[index + 1:])
    return root


def tree_inorder(root):
    if not root:
        return root
    tree_inorder(root.left)
    print root.value
    tree_inorder(root.right)


def tree_preorder(root):
    if not root:
        return root
    print root.value
    tree_inorder(root.left)
    tree_inorder(root.right)


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = bt_from_preorder_and_inorder(preorder, inorder)
    tree_inorder(root)
    tree_preorder(root)
