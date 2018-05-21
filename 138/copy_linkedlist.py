class LinkedList():

    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.random = None


def print_list(l):
    cache = []
    cache2 = []
    while l is not None:
        cache.append(l.value)
        cache2.append(l.random.value)
        l = l.next
    print cache
    print cache2


def copy_linkedlist(l):
    head = l
    while l:
        temp = l.next
        l.next = LinkedList(l.value)
        l.next.next = temp
        l = temp
    l = head
    while l:
        l.next.random = l.random.next
        l = l.next.next
    l = head.next
    while l.next:
        l.next = l.next.next
        l = l.next
    return head.next


if __name__ == '__main__':
    head = LinkedList(1)
    head.next = LinkedList(2)
    head.next.next = LinkedList(3)
    head.random = head
    head.next.random = head
    head.next.next.random = head
    print_list(copy_linkedlist(head))
