from linked_list import print_list, LinkedList, generate_list


def helper(l, n):
    prev = LinkedList()
    prev.next = l
    curr = l
    tail = curr
    count = 1
    while curr and count <= n:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count += 1
    tail.next = curr
    return prev


def reverse(l, m, n):
    head = l
    curr = l
    count = 1
    while curr:
        if count == m - 1:
            print curr.value
            curr.next = helper(curr.next, n - count)
            break
        count += 1
        curr = curr.next
    return head


if __name__ == '__main__':
    l = generate_list(range(1, 2))
    m = 1
    n = 1
    print_list(reverse(l, m, n))
