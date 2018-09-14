from tree import TreeNode


def helper(root, t, k, res):
    if not root:
        return
    helper(root.left, t, k, res)
    if len(res) < k:
        res.append(root.value)
    else:
        if abs(root.value - t) < abs(res[0] - t):
            del res[0]
            res.append(root.value)
    helper(root.right, t, k, res)


def closest(root, t, k):
    res = []
    helper(root, t, k, res)
    return res


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(30)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(29)
    root.right.right = TreeNode(100)
    t = 25
    k = 3
    print closest(root, t, k)
