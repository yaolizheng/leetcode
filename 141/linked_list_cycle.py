from linked_list import LinkedList


def has_cycle(head):
    slow = head
    fast = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


if __name__ == '__main__':
    head = LinkedList(1)
    head.next = LinkedList(2)
    head.next.next = LinkedList(3)
    head.next.next.next = head
    print has_cycle(head)
