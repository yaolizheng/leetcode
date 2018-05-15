from tree import TreeNode


def next_right(root):
    new_root = root
    while root:
        head = TreeNode(0)
        curr = head
        while root:
            if root.left:
                curr.next = root.left
                curr = curr.next
            if root.right:
                curr.next = root.right
                curr = curr.next
            root = root.next
        root = head.next
    return new_root

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(7)
    new_root = next_right(root)
    for x in [new_root, new_root.left, new_root.left.left]:
        cache = []
        while x:
            cache.append(x.value)
            x = x.next
        print cache
