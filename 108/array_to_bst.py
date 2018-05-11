from tree import TreeNode


def sorted_list_to_bst(l):
    if len(l) == 0:
        return None
    mid = len(l) / 2
    root = TreeNode(l[mid])
    root.left = sorted_list_to_bst(l[:mid])
    root.right = sorted_list_to_bst(l[mid + 1:])
    return root


def inorder(root):
    if not root:
        return root
    inorder(root.left)
    print root.value
    inorder(root.right)


if __name__ == '__main__':
    l = [-10, -3, 0, 5, 9]
    root = sorted_list_to_bst(l)
    inorder(root)
