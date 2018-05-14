from tree import TreeNode
from linked_list import LinkedList, print_list


def tree_to_list(root):
    if not root:
        return root
    new_head = head = LinkedList(root.value)
    right = tree_to_list(root.right)
    head.next = tree_to_list(root.left)
    while head.next:
        head = head.next
    head.next = right
    return new_head


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    print_list(tree_to_list(root))
