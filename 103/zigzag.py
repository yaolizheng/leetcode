from tree import TreeNode


def zigzag(root):
    l = [root]
    res = [[root.value]]
    level = 0
    while len(l) > 0:
        next_l = []
        for node in l:
            if node.left:
                next_l.append(node.left)
            if node.right:
                next_l.append(node.right)
        level += 1
        if next_l:
            temp = [x.value for x in next_l]
            if level % 2:
                temp.reverse()
            res.append(temp)
        l = next_l
    return res


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print zigzag(root)
