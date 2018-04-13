from linked_list import LinkedList, print_list


def swap(l):
    if l is None:
        return None
    if l.next is None:
        return l
    next = l.next
    next_next = next.next
    next.next = l
    head = next
    l.next = swap(next_next)
    return head


if __name__ == '__main__':
    l = LinkedList(1)
    l.next = LinkedList(2)
    l.next.next = LinkedList(3)
    l.next.next.next = LinkedList(4)
    print_list(swap(l))
