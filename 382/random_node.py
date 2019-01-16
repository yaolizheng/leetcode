from linked_list import LinkedList
import random


class solution:

    def __init__(self, head):
        self.head = head

    def getRandom(self):
        res = self.head
        cur = self.head.next
        i = 1
        while cur:
            j = random.randint(0, i)
            if j == 0:
                res = cur
            i += 1
            cur = cur.next
        return res


if __name__ == '__main__':
    head = LinkedList(0)
    head.next = LinkedList(1)
    head.next.next = LinkedList(2)
    test = solution(head)
    print test.getRandom().value
