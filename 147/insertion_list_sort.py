def print_list(l):
    cache = []
    while l is not None:
        cache.append(l.value)
        l = l.next
    print cache


class LinkedList():

    def __init__(self, value=None):
        self.value = value
        self.next = None


def insertion_list_sort(head):
    h = head
    t = head
    c = head
    while c:
        prev = LinkedList(0)
        prev.next = h
        curr = h
        next = c.next
        while curr:
            if curr.value > c.value:
                break
            curr = curr.next
            prev = prev.next
        if prev.next == h:
            c.next = h
            h = c
        elif curr is None:
            t.next = c
            t = c
        else:
            prev.next = c
            c.next = curr
        c = next
        t.next = None
    return h


if __name__ == '__main__':
    head = LinkedList(4)
    head.next = LinkedList(2)
    head.next.next = LinkedList(1)
    head.next.next.next = LinkedList(3)
    print_list(insertion_list_sort(head))
