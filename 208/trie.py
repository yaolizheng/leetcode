class TrieNode:

    def __init__(self):
        self.nodes = [None] * 26
        self.is_end = False


class Trie:

    def __init__(self):
        self.t = TrieNode()

    def insert(self, word):
        t = self.t
        for x in word:
            key = ord(x) - ord('a')
            if t.nodes[key] is None:
                t.nodes[key] = TrieNode()
            t = t.nodes[key]
        t.is_end = True

    def search(self, keyword):
        t = self.t
        for x in keyword:
            key = ord(x) - ord('a')
            if t.nodes[key] is not None:
                t = t.nodes[key]
            else:
                return False
        return t.is_end

    def starts_with(self, prefix):
        t = self.t
        for x in prefix:
            key = ord(x) - ord('a')
            if t.nodes[key] is not None:
                t = t.nodes[key]
            else:
                return False
        return True


if __name__ == '__main__':
    t = Trie()
    t.insert('apple')
    print t.search('app')
    print t.starts_with('app')
