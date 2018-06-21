def schedule(n, d):
    visited = set()
    stack = set()
    for x in d:
        if x[0] not in visited:
            if not bfs(x[0], d, visited, stack):
                return False
    return True


def bfs(i, d, visited, stack):
    visited.add(i)
    stack.add(i)
    for x in d:
        if x[0] == i:
            for j in range(1, len(x)):
                if x[j] not in visited:
                    if not bfs(x[j], d, visited, stack):
                        return False
                elif x[j] in stack:
                    return False
    stack.remove(i)
    return True


if __name__ == '__main__':
    n = 3
    d = [[1, 0, 2], [2, 0], [0, 1]]
    print schedule(n, d)
