class LinkedList():

    def __init__(self, value=None, key=None):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None


class LRU:

    def __init__(self, capacity):
        self.cache = dict()
        self.head = LinkedList(0, 0)
        self.tail = LinkedList(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            del self.cache[node.key]
        node = LinkedList(value, key)
        self.add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            old = self.head.next
            del self.cache[old.key]
            self.remove(old)

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return self.cache[key].value
        else:
            return -1


if __name__ == '__main__':
    cache = LRU(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print cache.get(1)
    cache.put(3, 3)
    print cache.get(2)
    cache.put(4, 4)
    print cache.get(1)
    print cache.get(3)
    print cache.get(4)
