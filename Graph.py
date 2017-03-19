class Graph:
    def __init__(self):
        self.masterlist = {}
        self.size = 0

    def add_vertex(self, vert):
        self.size += 1
        self.masterlist[vert] = Vertex(vert)

    def add_edge(self, fromvert, tovert, cost=0):
        if fromvert not in self.masterlist:
            self.add_vertex(fromvert)
        if tovert not in self.masterlist:
            self.add_vertex(tovert)

        self.masterlist[fromvert].add_neighbour(
            self.masterlist[tovert], cost)

    def get_vertex(self, vertkey):
        return self.masterlist.get(vertkey)

    def get_vertices(self):
        return self.masterlist.keys()

    def __contains__(self, vertkey):
        return vertkey in self.masterlist

    def __iter__(self):
        return iter(self.masterlist.values())

    def transpose(self):
        g = Graph()
        for vertex in self:
            for adj in vertex.get_connections():
                g.add_edge(adj.key, vertex.key)
        return g


class Vertex:
    def __init__(self, key):
        self.key = key
        self.connectedto = {}
        self.color = 'white'
        self.distance = 10000
        self.predecessor = None

    def add_neighbour(self, vert, weight=0):
        self.connectedto[vert] = weight

    def get_connections(self):
        return self.connectedto.keys()

    def __lt__(self, other):
        return self.distance < other.distance


if __name__ == '__main__':
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('C', 'A')
    gt = g.transpose()

    for vertex in gt:
        for adj in vertex.get_connections():
            print(vertex.key,'-->',adj.key)




