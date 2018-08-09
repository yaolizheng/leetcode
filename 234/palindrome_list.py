from linked_list import LinkedList


def compare(l1, l2):
    while l2:
        if l1 is None:
            return False
        if l1.value != l2.value:
            return False
        l1 = l1.next
        l2 = l2.next
    return True


def reverse(l):
    prev = None
    while l:
        temp = l.next
        l.next = prev
        prev = l
        l = temp
    return prev


def palindrome_list(l):
    l1 = l
    l2 = l
    while l2 and l2.next:
        l1 = l1.next
        l2 = l2.next.next
    return compare(l, reverse(l1))


if __name__ == '__main__':
    l = LinkedList(1)
    l.next = LinkedList(2)
    l.next.next = LinkedList(2)
    l.next.next.next = LinkedList(2)
    print palindrome_list(l)
