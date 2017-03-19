from Graph import Graph
from minHeap import minHeap


def prim(graph, start):
    pq = minHeap()
    start.distance = 0
    pq.build_heap([(vertex.distance, vertex) for vertex in graph])

    res = []
    while pq.size > 0:
        vertex = pq.del_min()[1]
        if vertex.predecessor:
            res.append((vertex.predecessor.key, vertex.key))
        for adj in vertex.get_connections():
            new_distance = vertex.distance + vertex.connectedto[adj]
            if (adj.distance,adj) in pq and new_distance < adj.distance:
                adj.distance = new_distance
                adj.predecessor = vertex
                pq.decrease_key(adj, new_distance)

    return res

g = Graph()
g.add_edge('A', 'B', 2)
g.add_edge('B', 'A', 2)
g.add_edge('A', 'C', 4)
g.add_edge('C', 'A', 4)
g.add_edge('B', 'C', 1)
g.add_edge('C', 'B', 1)
g.add_edge('B', 'D', 1)
g.add_edge('D', 'B', 1)
g.add_edge('B', 'E', 4)
g.add_edge('E', 'B', 4)
g.add_edge('D', 'E', 1)
g.add_edge('E', 'D', 1)
g.add_edge('C', 'F', 5)
g.add_edge('F', 'C', 5)
g.add_edge('E', 'F', 1)
g.add_edge('F', 'E', 1)
g.add_edge('F', 'G', 1)
g.add_edge('G', 'F', 1)

print(g.get_vertex('A').connectedto)
print(prim(g, g.get_vertex('A')))

