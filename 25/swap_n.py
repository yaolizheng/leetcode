from linked_list import LinkedList, print_list


def reverse(l):
    prev = None
    curr = l
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def swap_n(l, n):
    if l is None:
        return None
    prev = None
    curr = l
    i = 0
    tail = curr
    while curr and i < n:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        i += 1
    tail.next = swap_n(next, n)
    return prev

if __name__ == '__main__':
    l = LinkedList(1)
    l.next = LinkedList(2)
    l.next.next = LinkedList(3)
    l.next.next.next = LinkedList(4)
    l.next.next.next.next = LinkedList(5)
    # print_list(swap_n(l, 2))
    print_list(swap_n(l, 3))
