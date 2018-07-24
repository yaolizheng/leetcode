class TrieNode:

    def __init__(self):
        self.nodes = [None] * 26
        self.is_end = False


class Trie:

    def __init__(self):
        self.t = TrieNode()

    def addWord(self, word):
        t = self.t
        for x in word:
            key = ord(x) - ord('a')
            if t.nodes[key] is None:
                t.nodes[key] = TrieNode()
            t = t.nodes[key]
        t.is_end = True

    def search(self, keyword):
        return self.search_util(keyword, 0, self.t)

    def search_util(self, keyword, i, trie):
        if i == len(keyword):
            return trie.is_end
        if keyword[i] == '.':
            for t in trie.nodes:
                if t is not None:
                    return self.search_util(keyword, i + 1, t)
        else:
            key = ord(keyword[i]) - ord('a')
            if trie.nodes[key] is not None:
                return self.search_util(keyword, i + 1, trie.nodes[key])
            else:
                return False


if __name__ == '__main__':
    t = Trie()
    t.addWord('bad')
    t.addWord('dad')
    t.addWord('mad')
    print t.search('pad')
    print t.search('bad')
    print t.search('.ad')
    print t.search('...')
