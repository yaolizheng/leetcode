from tree import sample


def helper(root, node, succ):
    if not root:
        return succ
    if root.value > node:
        succ = root.value
        return helper(root.left, node, succ)
    elif root.value < node:
        return helper(root.right, node, succ)
    else:
        root = root.right
        while root:
            succ = root.value
            root = root.left
        return succ


def successor(root, node):
    return helper(root, node, None)


if __name__ == '__main__':
    root = sample()
    print successor(root, 6)
