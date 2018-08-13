from linked_list import LinkedList, print_list


def delete2(head, n):
    cur = head
    new_head = LinkedList(0)
    new_head.next = head
    prev = new_head
    while cur:
        if cur.value == n:
            prev.next = cur.next
            break
        prev = prev.next
        cur = cur.next
    return new_head.next


def delete(node):
    node.value = node.next.value
    node.next = node.next.next


if __name__ == '__main__':
    head = LinkedList(4)
    head.next = LinkedList(5)
    head.next.next = LinkedList(1)
    node = head.next
    head.next.next.next = LinkedList(9)
    delete(node)
    print_list(head)
