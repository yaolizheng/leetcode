from linked_list import LinkedList, print_list


def remove_element(l, val):
    head = LinkedList(0)
    head.next = l
    res = head.next
    while head and head.next:
        if head.next.value == val:
            head.next = head.next.next
        else:
            head = head.next
    return res


if __name__ == '__main__':
    head = LinkedList(1)
    head.next = LinkedList(2)
    head.next.next = LinkedList(6)
    head.next.next.next = LinkedList(3)
    head.next.next.next.next = LinkedList(5)
    head.next.next.next.next.next = LinkedList(6)
    print_list(remove_element(head, 6))
