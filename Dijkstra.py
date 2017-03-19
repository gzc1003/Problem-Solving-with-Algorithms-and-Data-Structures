from Graph import Graph
from minHeap import minHeap


def dijkstra(graph, start):
    start.distance = 0

    alist = [(vert.distance, vert) for vert in graph]

    priority_queue = minHeap()
    priority_queue.build_heap(alist)

    while priority_queue.size > 0:
        vertex = priority_queue.del_min()[1]
        for adj in vertex.get_connections():
            if adj.distance > vertex.distance + vertex.connectedto[adj]:
                adj.distance = vertex.distance + vertex.connectedto[adj]
                adj.predecessor = vertex
                priority_queue.decrease_key(adj,adj.distance)


g = Graph()
g.add_edge('u', 'v', 2)
g.add_edge('v', 'u', 2)
g.add_edge('u', 'x', 1)
g.add_edge('x', 'u', 1)
g.add_edge('v', 'x', 2)
g.add_edge('x', 'v', 2)
g.add_edge('v', 'w', 3)
g.add_edge('w', 'v', 3)
g.add_edge('w', 'y', 1)
g.add_edge('y', 'w', 1)
g.add_edge('w', 'x', 3)
g.add_edge('x', 'w', 3)
g.add_edge('x', 'y', 1)
g.add_edge('y', 'x', 1)
g.add_edge('w', 'z', 5)
g.add_edge('z', 'w', 5)
g.add_edge('y', 'z', 1)
g.add_edge('z', 'y', 1)

dijkstra(g, g.get_vertex('u'))

vertex = g.get_vertex('z')
stack = []
while vertex:
    stack.insert(0, vertex.key)
    vertex = vertex.predecessor
print(stack)

print('u', g.get_vertex('u').distance)
print('v', g.get_vertex('v').distance)
print('w', g.get_vertex('w').distance)
print('z', g.get_vertex('z').distance)
print('x', g.get_vertex('x').distance)
print('y', g.get_vertex('y').distance)

print(g.size)


