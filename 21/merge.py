from linked_list import LinkedList, print_list


def merge(l1, l2):
    head = l = LinkedList(0)
    while l1 and l2:
        if l1.value > l2.value:
            l.next = LinkedList(l2.value)
            l2 = l2.next
        else:
            l.next = LinkedList(l1.value)
            l1 = l1.next
        l = l.next
    if l1:
        l.next = l1
    if l2:
        l.next = l2
    return head.next


if __name__ == '__main__':
    l1 = LinkedList(1)
    l1.next = LinkedList(2)
    l1.next.next = LinkedList(4)
    l2 = LinkedList(1)
    l2.next = LinkedList(3)
    l2.next.next = LinkedList(4)
    print_list(merge(l1, l2))
