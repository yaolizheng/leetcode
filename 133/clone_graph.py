class Graph:

    def __init__(self, label=None):
        self.label = label
        self.neighbors = []


def helper(g):
    if g.label in helper.map:
        return helper.map[g.label]
    clone_node = Graph(g.label)
    helper.map[g.label] = clone_node
    for neighbor in g.neighbors:
        clone_node.neighbors.append(helper(neighbor))
    return clone_node


def clone_graph(g):
    helper.map = dict()
    return helper(g)


if __name__ == '__main__':
    test = Graph(1)
    test.neighbors.append(Graph(2))
    test.neighbors.append(Graph(3))
    res = clone_graph(test)
    print res.label, res.neighbors[0].label, res.neighbors[1].label
