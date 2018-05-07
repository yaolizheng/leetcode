class LinkedList():

    def __init__(self, value=None):
        self.value = value
        self.next = None


def print_list(l):
    cache = []
    while l is not None:
        cache.append(l.value)
        l = l.next
    print cache


def generate_list(nums):
    head = LinkedList()
    curr = head
    for x in nums:
        curr.next = LinkedList(x)
        curr = curr.next
    return head.next
