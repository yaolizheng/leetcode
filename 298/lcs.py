from tree import sample


def helper(root, expect, length):
    if not root:
        return
    if root.value == expect:
        length += 1
    else:
        length = 1
    helper.max = max(helper.max, length)
    helper(root.left, root.value + 1, length)
    helper(root.right, root.value + 1, length)


def lcs(root):
    helper.max = 1
    helper(root, root.value, 0)
    return helper.max


if __name__ == '__main__':
    root = sample()
    print lcs(root)
