from linked_list import print_list, LinkedList


def partition(l, x):
    small = LinkedList(0)
    small_header = small
    large = LinkedList(0)
    large_header = large
    cur = l
    while cur:
        if cur.value < x:
            small.next = cur
            small = small.next
        else:
            large.next = cur
            large = large.next
        cur = cur.next
    small.next = large_header.next
    large.next = None
    return small_header.next


if __name__ == '__main__':
    l = LinkedList(1)
    l.next = LinkedList(4)
    l.next.next = LinkedList(3)
    l.next.next.next = LinkedList(2)
    l.next.next.next.next = LinkedList(5)
    l.next.next.next.next.next = LinkedList(2)
    x = 3
    print_list(partition(l, x))
