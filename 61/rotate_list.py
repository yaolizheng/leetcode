from linked_list import LinkedList, print_list


def length(l):
    cur = l
    count = 0
    while cur:
        cur = cur.next
        count += 1
    return count


def rotate_list(l, k):
    head = l
    cur = prev = l
    k = k % length(l)
    for _ in range(k):
        cur = cur.next
    while cur.next:
        prev = prev.next
        cur = cur.next
    new_head = prev.next
    cur.next = head
    prev.next = None
    return new_head


if __name__ == '__main__':
    root = LinkedList(1)
    root.next = LinkedList(2)
    root.next.next = LinkedList(3)
    root.next.next.next = LinkedList(4)
    root.next.next.next.next = LinkedList(5)
    k = 8
    print_list(rotate_list(root, k))
