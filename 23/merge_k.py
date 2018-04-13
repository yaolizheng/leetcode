from linked_list import LinkedList, print_list
import heapq


def merge_k(l):
    heap = list()
    for _list in l:
        while _list:
            heapq.heappush(heap, _list.value)
            _list = _list.next
    head = point = LinkedList(0)
    while len(heap):
        point.next = LinkedList(heapq.heappop(heap))
        point = point.next
    return head.next

if __name__ == '__main__':
    l1 = LinkedList(1)
    l1.next = LinkedList(4)
    l1.next.next = LinkedList(5)
    l2 = LinkedList(1)
    l2.next = LinkedList(3)
    l2.next.next = LinkedList(4)
    l3 = LinkedList(2)
    l3.next = LinkedList(6)
    l = [l1, l2, l3]
    print_list(merge_k(l))
