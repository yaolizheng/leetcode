from linked_list import LinkedList, print_list


def remove_nth_from_end(root, n):
    head = l1 = l2 = root
    for i in range(n):
        l2 = l2.next
    while l2.next:
        l2 = l2.next
        l1 = l1.next
    l1.next = l1.next.next
    return head

if __name__ == '__main__':
    root = LinkedList(1)
    root.next = LinkedList(2)
    root.next.next = LinkedList(3)
    root.next.next.next = LinkedList(4)
    root.next.next.next.next = LinkedList(5)
    print_list(remove_nth_from_end(root, 2))
