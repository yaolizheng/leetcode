from tree import TreeNode


def preorder(root, res):
    if not root:
        res.append(None)
        return root
    res.append(root.value)
    preorder(root.left, res)
    preorder(root.right, res)


def helper(vals):
    if not vals:
        return [None]
    if len(vals) == 1:
        return [TreeNode(vals[0])]
    res = []
    for i in range(len(vals)):
        left = helper(vals[:i])
        right = helper(vals[i + 1:])
        for l in left:
            for r in right:
                node = TreeNode(vals[i])
                node.left = l
                node.right = r
                res.append(node)
    return res


def unique_bst(n):
    l = range(1, n + 1)
    res = helper(l)
    return res


if __name__ == '__main__':
    n = 3
    for x in unique_bst(n):
        res = []
        preorder(x, res)
        print res
        print '------------------'
