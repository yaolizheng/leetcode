from tree import TreeNode


def kth_small(root, k):
    stack = []
    current = root
    count = 1
    while True:
        if current:
            stack.append(current)
            current = current.left
        else:
            if len(stack) != 0:
                temp = stack.pop()
                if count == k:
                    return temp.value
                current = temp.right
                count += 1
            else:
                break


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    k = 3
    print kth_small(root, k)
