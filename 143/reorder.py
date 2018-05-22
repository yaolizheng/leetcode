from linked_list import LinkedList, print_list


def reverse(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


def reorder(head):
    fast = head
    slow = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    temp = slow.next
    slow.next = None
    next = reverse(temp)
    new_head = LinkedList(0)
    curr = new_head
    while head or next:
        if head:
            curr.next = head
            curr = curr.next
            head = head.next
        if next:
            curr.next = next
            curr = curr.next
            next = next.next
    return new_head.next


if __name__ == '__main__':
    head = LinkedList(1)
    head.next = LinkedList(2)
    head.next.next = LinkedList(3)
    head.next.next.next = LinkedList(4)
    head.next.next.next.next = LinkedList(5)
    print_list(reorder(head))
