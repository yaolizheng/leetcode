from tree import TreeNode


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root.value
    inorder(root.right)


def inorder_iter(root):
    stack = []
    curr = root
    while True:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            if len(stack) == 0:
                break
            curr = stack.pop()
            print curr.value
            curr = curr.right


if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    inorder_iter(root)
