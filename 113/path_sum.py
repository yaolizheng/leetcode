from tree import TreeNode


def helper(root, num, temp, res):
    if not root:
        return
    if not root.left and not root.right and num == root.value:
        res.append(temp + [root.value])
        return
    helper(root.left, num - root.value, temp + [root.value], res)
    helper(root.right, num - root.value, temp + [root.value], res)


def path_sum(root, num):
    res = []
    helper(root, num, [], res)
    return res


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    num = 22
    print path_sum(root, num)
