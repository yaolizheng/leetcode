from tree import TreeNode


class Iterator:

    def __init__(self, root):
        self.root = root
        self.stack = []
        self.push_left(self.root)

    def push_left(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return len(self.stack) != 0

    def next(self):
        res = self.stack.pop()
        self.push_left(res.right)
        return res.value


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    i = Iterator(root)
    while i.hasNext():
        print i.next()
