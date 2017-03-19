from collections import deque


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


class Vertex:
    def __init__(self, key):
        self.key = key
        self.connectedto = {}
        self.color = 'white'
        self.predecessor = set()

    def add_neighbour(self, vert, weight=0):
        self.connectedto[vert] = weight

    def get_connections(self):
        return self.connectedto.keys()


def find_all_path(graph, start, end):
    res = []
    bfs(graph, start)
    find_all_path_helper(start, end, [end.key], res)
    return res


def bfs(graph, start):
    queue = deque()
    queue.append(start)
    while queue:
        vertex = queue.popleft()
        for adj in vertex.get_connections():
            if adj.color == 'white':
                adj.color = 'grey'
                queue.append(adj)
            adj.predecessor.add(vertex)


def find_all_path_helper(start, end, path, res):
    if start.key == end.key:
        res.append(path.copy())

    else:
        for vert in end.predecessor:
            if vert.key not in path:
                path.insert(0, vert.key)
                find_all_path_helper(start, vert, path, res)

    path.pop(0)


g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('B', 'D')
g.add_edge('D', 'E')
g.add_edge('C', 'E')

res = find_all_path(g, g.get_vertex('A'), g.get_vertex('E'))

for path in res:
    print(path)
