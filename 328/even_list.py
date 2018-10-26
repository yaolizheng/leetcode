from linked_list import LinkedList, print_list


def even_list(head):
    prev = head
    cur = head.next
    while cur and cur.next:
        tmp = prev.next
        prev.next = cur.next
        cur.next = cur.next.next
        prev.next.next = tmp
        cur = cur.next
        prev = prev.next
    return head


if __name__ == '__main__':
    head = LinkedList(1)
    head.next = LinkedList(2)
    head.next.next = LinkedList(3)
    head.next.next.next = LinkedList(4)
    head.next.next.next.next = LinkedList(5)
    print_list(even_list(head))
