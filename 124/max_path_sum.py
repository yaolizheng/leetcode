from tree import TreeNode
import sys


def max_path_sum(root):
    helper.res = -sys.maxint - 1
    helper(root)
    return helper.res


def helper(root):
    if not root:
        return 0
    max_left = helper(root.left)
    max_right = helper(root.right)
    single_max = max(max(max_left, max_right) + root.value, root.value)
    total_max = max(single_max, max_left + max_right + root.value)
    helper.res = max(helper.res, total_max)
    return single_max


if __name__ == '__main__':
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print max_path_sum(root)
