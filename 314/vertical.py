from tree import sample


def helper(root, dis):
    if not root:
        return
    if dis not in helper.result:
        helper.result[dis] = []
    helper.result[dis].append(root.value)
    helper(root.left, dis - 1)
    helper(root.right, dis + 1)


def vertical(root):
    helper.result = dict()
    helper(root, 0)
    keys = sorted(helper.result.keys())
    res = []
    for key in keys:
        res.append(helper.result[key])
    return res


if __name__ == '__main__':
    root = sample()
    print vertical(root)
