from tree import TreeNode


def next_right(root):
    if not root:
        return root
    l = [root]
    res = []
    while len(l) > 0:
        node = TreeNode(0)
        head = node
        next_l = []
        while len(l) > 0:
            next_node = l.pop(0)
            if next_node.left:
                next_l.append(next_node.left)
            if next_node.right:
                next_l.append(next_node.right)
            node.next = next_node
            node = next_node
        l = next_l
        res.append(head.next)
    return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    for x in next_right(root):
        cache = []
        while x:
            cache.append(x.value)
            x = x.next
        print cache
