class graph:

    def __init__(self, n, e):
        self.n = n
        self.g = dict()
        self.degree = dict()
        for _e in e:
            self.add(_e[0], _e[1])

    def add(self, a, b):
        if a not in self.g:
            self.g[a] = list()
        if b not in self.g:
            self.g[b] = list()
        self.g[b].append(a)
        if a not in self.degree:
            self.degree[a] = 0
        if b not in self.degree:
            self.degree[b] = 0
        self.degree[a] += 1
        self.degree[b] += 1

    def mht(self):
        q = list()
        for n in self.degree:
            if self.degree[n] == 1:
                q.append(n)
        while self.n > 2:
            for _ in range(len(q)):
                n = q.pop(0)
                self.n -= 1
                for next in self.g[n]:
                    self.degree[next] -= 1
                    if self.degree[next] == 1:
                        q.append(next)
        return q


if __name__ == '__main__':
    n = 4
    e = [[1, 0], [1, 2], [1, 3]]
    test = graph(n, e)
    print test.mht()
