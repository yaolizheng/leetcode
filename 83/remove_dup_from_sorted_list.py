from linked_list import print_list, LinkedList


def remove_dup_from_sorted_list(head):
    new_head = LinkedList(0)
    prev = new_head
    new_head.next = head
    cur = head
    while cur.next:
        if cur.value != cur.next.value:
            prev.next = cur
            prev = prev.next
        cur = cur.next
    prev.next = cur
    return new_head.next


if __name__ == '__main__':
    head = LinkedList(1)
    head.next = LinkedList(2)
    head.next.next = LinkedList(3)
    head.next.next.next = LinkedList(3)
    head.next.next.next.next = LinkedList(4)
    head.next.next.next.next.next = LinkedList(4)
    head.next.next.next.next.next.next = LinkedList(4)
    print_list(remove_dup_from_sorted_list(head))
