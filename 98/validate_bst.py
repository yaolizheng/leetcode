from tree import TreeNode
import sys


def helper(root, max, min):
    if not root:
        return True
    if root.value > max or root.value < min:
        return False
    return helper(root.left, root.value, min) and helper(root.right, max, root.value)


def validate_bst(root):
    return helper(root, sys.maxint, -sys.maxint - 1)


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print validate_bst(root)
