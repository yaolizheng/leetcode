from linked_list import LinkedList


def intersection_list(h1, h2):
    temp1 = h1
    temp2 = h2
    reach_end = False
    while h1 and h2:
        if h1 == h2:
            return h1.value
        if not h1.next:
            if not reach_end:
                reach_end = True
            else:
                return None
            h1 = temp2
        else:
            h1 = h1.next
        if not h2.next:
            h2 = temp1
        else:
            h2 = h2.next


if __name__ == '__main__':
    head1 = LinkedList(1)
    head1.next = LinkedList(2)
    head2 = LinkedList(10)
    head2.next = LinkedList(11)
    head2.next.next = LinkedList(12)
    intersection = LinkedList(100)
    head1.next.next = intersection
    head2.next.next.next = intersection
    intersection.next = LinkedList(101)
    intersection.next.next = LinkedList(102)
    print intersection_list(head1, head2)
