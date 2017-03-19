from collections import deque

from Graph import Graph


def all_pairs_shortest_path(graph):
    all_path = []
    for start in graph:
        BFS(graph, start.key)
        for end in graph:
            path = []
            if end == start:
                continue
            elif end.predecessor is None:
                path.append("can not reach %s" % end.key)
            else:
                while end:
                    path.insert(0, end.key)
                    end = end.predecessor

            all_path.append(path)
    return all_path


def BFS(graph, start):
    for vertex in graph:
        vertex.distance = 0
        vertex.predecessor = None
        vertex.color = 'white'

    queue = deque()
    start_vertex = graph.get_vertex(start)
    start_vertex.color = 'gray'
    queue.append(start_vertex)

    while queue:
        current = queue.popleft()
        for adj in current.get_connections():
            if adj.color == 'white':
                adj.color = 'gray'
                adj.predecessor = current
                adj.distance = current.distance + 1
                queue.append(adj)
        current.color = 'black'


g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('D', 'E')
g.add_edge('D', 'C')
g.add_edge('D', 'F')
g.add_edge('E', 'F')
g.add_edge('C', 'E')
print(all_pairs_shortest_path(g))
