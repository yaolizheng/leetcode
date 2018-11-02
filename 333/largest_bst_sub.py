from tree import TreeNode
import sys


def helper(root, mn, mx, res):
    if not root:
        return True, -sys.maxint + 1, sys.maxint, res
    left_mx = sys.maxint
    right_mx = sys.maxint
    left_mn = -sys.maxint + 1
    right_mn = -sys.maxint + 1
    left_n = 0
    right_n = 0
    left, left_mn, left_mx, left_n = helper(root.left, left_mn, left_mx, left_n)
    right, right_mn, right_mx, right_n = helper(root.right, right_mn, right_mx, right_n)
    if left and right:
        if (root.left is None or root.value > left_mx) and (root.right is None or root.value < right_mx):
            res = left_n + right_n + 1
            mn = left_mn if root.left else root.value
            mx = right_mx if root.right else root.value
            return True, mn, mx, res
    res = max(left_n, right_n)
    return False, None, None, res


def largest_bst_sub(root):
    _, _, _, res = helper(root, -sys.maxint + 1, sys.maxint, 0)
    return res


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(8)
    root.right.right = TreeNode(7)
    print largest_bst_sub(root)
