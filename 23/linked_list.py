class LinkedList():

    def __init__(self, value=None):
        self.value = value
        self.next = None


def print_list(l):
    while l is not None:
        print l.value
        l = l.next
