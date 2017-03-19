from Graph import Graph


def topological_sort(graph):
    stack = []
    for vertex in graph:
        if vertex.color == 'white':
            dfs_visit(vertex,stack)

    return stack


def dfs_visit(vertex,stack):
    vertex.color = 'grey'
    for neighbour in vertex.get_connections():
        if neighbour.color == 'white':
            neighbour.predecessor = vertex
            dfs_visit(neighbour,stack)

    stack.insert(0,vertex.key)
    vertex.color = 'black'


g = Graph()

g.add_edge('A','C')
g.add_edge('B','C')
g.add_edge('C','D')
g.add_edge('E','D')
g.add_edge('D','F')
g.add_edge('F','G')
g.add_edge('C','H')
g.add_edge('H','G')

print(topological_sort(g))

