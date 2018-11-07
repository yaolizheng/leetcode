class TreeNode:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def sample():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    return root
