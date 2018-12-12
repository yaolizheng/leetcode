from linked_list import LinkedList, print_list


def plus_one(head):
    carry = helper(head)
    if carry == 1:
        new_head = LinkedList(1)
        new_head.next = head
        return new_head
    return head


def helper(head):
    if not head:
        return 1
    carry = helper(head.next)
    s = head.value + carry
    head.value = s % 10
    return s / 10


if __name__ == '__main__':
    head = LinkedList(9)
    head.next = LinkedList(9)
    head.next.next = LinkedList(9)
    res = plus_one(head)
    print_list(res)
