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


def sort_list(head):
    if not head or not head.next:
        return head
    fast = head
    slow = head
    prev = None
    while fast and fast.next:
        prev = slow
        fast = fast.next.next
        slow = slow.next
    prev.next = None
    l1 = sort_list(slow)
    l2 = sort_list(head)
    return merge_list(l1, l2)


def merge_list(l1, l2):
    l = LinkedList(0)
    head = l
    while l1 and l2:
        if l1.value < l2.value:
            l.next = LinkedList(l1.value)
            l = l.next
            l1 = l1.next
        else:
            l.next = LinkedList(l2.value)
            l = l.next
            l2 = l2.next
        if l1:
            l.next = l1
        if l2:
            l.next = l2
    return head.next


if __name__ == '__main__':
    head = LinkedList(4)
    head.next = LinkedList(2)
    head.next.next = LinkedList(1)
    head.next.next.next = LinkedList(3)
    print_list(sort_list(head))
