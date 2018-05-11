from tree import TreeNode
from linked_list import LinkedList


def list_to_bst(l):
    if not l:
        return None
    if not l.next:
        return TreeNode(l.value)
    fast = l
    slow = l
    prev = LinkedList(0)
    prev.next = l
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        prev = prev.next
    root = TreeNode(slow.value)
    prev.next = None
    root.left = list_to_bst(l)
    root.right = list_to_bst(slow.next)
    return root


def inorder(root):
    if not root:
        return root
    inorder(root.left)
    print root.value
    inorder(root.right)


if __name__ == '__main__':
    l = LinkedList(-10)
    l.next = LinkedList(-3)
    l.next.next = LinkedList(0)
    l.next.next.next = LinkedList(5)
    l.next.next.next.next = LinkedList(9)
    root = list_to_bst(l)
    inorder(root)
