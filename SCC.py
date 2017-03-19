class Graph:
    def __init__(self):
        self.masterlist = {}
        self.size = 0
        self.time = 1
        self.ascc = []
        self.sccs = []

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

    def dfs(self, vertices=None):
        if vertices is None:
            vertices = self

        for vertex in vertices:
            if vertex.color == 'white':
                self.ascc = []
                self.dfs_visit(vertex)
                self.sccs.append(self.ascc)

    def dfs_visit(self, vertex):
        vertex.color = 'grey'
        vertex.discovery_time = self.time
        self.ascc.append(vertex.key)
        for neighbour in vertex.get_connections():

            if neighbour.color == 'white':
                neighbour.predecessor = vertex
                self.time += 1
                self.dfs_visit(neighbour)

        self.time += 1
        vertex.finish_time = self.time
        vertex.color = 'black'

    def SCC(self):
        self.dfs()
        vertices = list(self)
        vertices.sort(key=lambda x: x.finish_time, reverse=True)

        gt = self.transpose()
        vertices = [gt.masterlist[vertex.key] for vertex in vertices]
        gt.dfs(vertices)

        return gt.sccs


class Vertex:
    def __init__(self, key):
        self.key = key
        self.connectedto = {}
        self.color = 'white'
        self.distance = 10000
        self.predecessor = None
        self.discovery_time = None
        self.finish_time = None

    def add_neighbour(self, vert, weight=0):
        self.connectedto[vert] = weight

    def get_connections(self):
        return self.connectedto.keys()

    def __lt__(self, other):
        return self.distance < other.distance


g = Graph()
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'F')
g.add_edge('F', 'H')
g.add_edge('H', 'I')
g.add_edge('I', 'F')
g.add_edge('B', 'E')
g.add_edge('E', 'D')
g.add_edge('D', 'B')
g.add_edge('E', 'A')
g.add_edge('D', 'G')
g.add_edge('G', 'E')

print(g.SCC())
