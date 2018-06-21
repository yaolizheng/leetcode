from linked_list import LinkedList, print_list


def reverse_list(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev


if __name__ == '__main__':
    head = LinkedList(1)
    # head.next = LinkedList(2)
    # head.next.next = LinkedList(3)
    # head.next.next.next = LinkedList(4)
    # head.next.next.next.next = LinkedList(5)
    print_list(reverse_list(head))
