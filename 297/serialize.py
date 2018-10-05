from tree import sample, TreeNode


def serialize(root):
    def preorder(root):
        if not root:
            res.append('#')
        else:
            res.append(str(root.value))
            preorder(root.left)
            preorder(root.right)
    res = []
    preorder(root)
    return ''.join(res)


def deserialize(s):
    def preorder(q):
        cur = q.pop(0)
        if cur == '#':
            return None
        root = TreeNode(int(cur))
        root.left = preorder(q)
        root.right = preorder(q)
        return root
    q = list(s)
    return preorder(q)


def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print root.value
    inorder(root.right)


if __name__ == '__main__':
    root = sample()
    s = serialize(root)
    print s
    d = deserialize(s)
    inorder(d)
