from tree import TreeNode


def side_view(root):
    queue = list()
    level = dict()
    queue.append((root, 0))
    while len(queue) > 0:
        node, l = queue.pop(0)
        level[l] = node.value
        if node.left:
            queue.append((node.left, l + 1))
        if node.right:
            queue.append((node.right, l + 1))
    return level.values()


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    print side_view(root)
