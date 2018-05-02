from linked_list import print_list, LinkedList


def remove_dup_from_sorted_list(head):
    new_head = LinkedList(0)
    prev = new_head
    new_head.next = head
    cur = head
    while cur:
        count = 0
        while(cur.next and cur.value == cur.next.value):
            count += 1
            cur = cur.next
        if count == 0:
            prev.next = cur
            prev = cur
        cur = cur.next
    prev.next = None
    return new_head.next


if __name__ == '__main__':
    head = LinkedList(1)
    head.next = LinkedList(2)
    head.next.next = LinkedList(3)
    head.next.next.next = LinkedList(3)
    head.next.next.next.next = LinkedList(4)
    head.next.next.next.next.next = LinkedList(4)
    head.next.next.next.next.next.next = LinkedList(5)
    print_list(remove_dup_from_sorted_list(head))
