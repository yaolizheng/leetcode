from tree import TreeNode


def level(root):
    l = [root]
    res = [[root.value]]
    while len(l) > 0:
        next_l = []
        for node in l:
            if node.left:
                next_l.append(node.left)
            if node.right:
                next_l.append(node.right)
        if next_l:
            res.append([x.value for x in next_l])
        l = next_l
    return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print level(root)
