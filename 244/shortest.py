import sys


class ShortestWordDistance:

    def __init__(self, words):
        self.word = dict()
        for i in range(len(words)):
            w = words[i]
            if w not in self.word:
                self.word[w] = list()
            self.word[w].append(i)

    def shortest_distance(self, a, b):
        i = j = 0
        res = sys.maxint
        while i < len(self.word[a]) and j < len(self.word[b]):
            res = min(res, abs(self.word[a][i] - self.word[b][j]))
            if self.word[a][i] < self.word[b][j]:
                i += 1
            else:
                j += 1
        return res


if __name__ == '__main__':
    words = ["practice", "makes", "perfect", "coding", "makes"]
    test = ShortestWordDistance(words)
    print test.shortest_distance('practice', 'makes')
