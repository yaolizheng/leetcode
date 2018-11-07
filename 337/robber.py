from tree import TreeNode


def helper(root, mapping):
    if not root:
        return 0
    if root in mapping:
        return mapping[root]
    val = 0
    if root.left:
        val += helper(root.left.left, mapping) + helper(root.left.right, mapping)
    if root.right:
        val += helper(root.right.left, mapping) + helper(root.right.right, mapping)
    val = max(root.value + val, helper(root.left, mapping) + helper(root.right, mapping))
    mapping[root] = val
    return val


def robber(root):
    mapping = dict()
    return helper(root, mapping)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)
    print robber(root)
