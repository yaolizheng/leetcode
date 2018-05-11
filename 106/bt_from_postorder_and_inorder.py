from tree import TreeNode


def bt_from_postorder_and_inorder(postorder, inorder):
    if len(postorder) <= 0:
        return None
    print postorder
    print inorder
    root = TreeNode(postorder[-1])
    index = inorder.index(postorder[-1])
    root.left = bt_from_postorder_and_inorder(postorder[:index], inorder[0:index])
    root.right = bt_from_postorder_and_inorder(postorder[index:-1], inorder[index + 1:])
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


def tree_postorder(root):
    if not root:
        return root
    tree_postorder(root.left)
    tree_postorder(root.right)
    print root.value


if __name__ == '__main__':
    postorder = [9, 15, 7, 20, 3]
    inorder = [9, 3, 15, 20, 7]
    root = bt_from_postorder_and_inorder(postorder, inorder)
    tree_postorder(root)
    tree_inorder(root)
