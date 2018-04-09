from linked_list import LinkedList, print_list


def add_two_numbers(num1, num2):
    carry = 0
    head = result = LinkedList(0)
    while num1 or num2 or carry != 0:
        a = 0 if num1 is None else num1.value
        b = 0 if num2 is None else num2.value
        sum = a + b + carry
        result.next = LinkedList(sum % 10)
        carry = sum / 10
        result = result.next
        num1 = num1.next if num1 is not None else None
        num2 = num2.next if num2 is not None else None
    return head.next


if __name__ == '__main__':
    root1 = LinkedList(2)
    root1.next = LinkedList(4)
    root1.next.next = LinkedList(3)
    root2 = LinkedList(5)
    root2.next = LinkedList(6)
    root2.next.next = LinkedList(4)
    print_list(add_two_numbers(root1, root2))
