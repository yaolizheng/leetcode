from tree import TreeNode


def helper(root):
    if not root:
        return
    helper(root.left)
    if helper.prev is not None and root.value < helper.prev.value:
        if helper.first is None:
            helper.first = helper.prev
            helper.middle = root
        else:
            helper.last = root
    helper.prev = root
    helper(root.right)


def recover_bst(root):
    helper.first = None
    helper.middle = None
    helper.last = None
    helper.prev = None
    helper(root)
    if helper.last:
        temp = helper.last.value
        helper.last.value = helper.first.value
        helper.first.value = temp
    else:
        temp = helper.middle.value
        helper.middle.value = helper.first.value
        helper.first.value = temp


def inorder(root):
    if not root:
        return root
    inorder(root.left)
    print root.value
    inorder(root.right)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.right = TreeNode(2)
    inorder(root)
    recover_bst(root)
    inorder(root)
