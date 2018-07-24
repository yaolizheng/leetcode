class TrieNode:

    def __init__(self):
        self.nodes = [None] * 26
        self.word = None


def search_word(board, words):
    t = buildNode(words)
    res = list()
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(board, i, j, t, res)
    return res


def dfs(board, i, j, t, res):
    c = board[i][j]
    if c == '*' or t.nodes[ord(c) - ord('a')] is None:
        return
    t = t.nodes[ord(c) - ord('a')]
    if t.word is not None:
        res.append(t.word)
        t.word = None
    board[i][j] = '*'
    if i > 0:
        dfs(board, i - 1, j, t, res)
    if j > 0:
        dfs(board, i, j - 1, t, res)
    if i < len(board) - 1:
        dfs(board, i + 1, j, t, res)
    if j < len(board[0]) - 1:
        dfs(board, i, j + 1, t, res)
    board[i][j] = c


def buildNode(words):
    t = TrieNode()
    for w in words:
        root = t
        for l in w:
            key = ord(l) - ord('a')
            if root.nodes[key] is not None:
                root = root.nodes[key]
            else:
                new_node = TrieNode()
                root.nodes[key] = new_node
                root = new_node
        root.word = w
    return t


if __name__ == '__main__':
    words = ["oath", "pea", "eat", "rain"]
    board = [['o', 'a', 'a', 'n'],
             ['e', 't', 'a', 'e'],
             ['i', 'h', 'k', 'r'],
             ['i', 'f', 'l', 'v']]
    print search_word(board, words)
