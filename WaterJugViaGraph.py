from collections import deque

from Graph import Graph


def water_jug(big, small, final):
    g = build_graph(big, small)
    BFS(g, (0, 0))
    possible_ends = [g.get_vertex((final, s)) for s in range(small+1) if g.get_vertex((final, s))]
    
    min_distance = 10000
    for end in possible_ends:

        if end.distance < min_distance:
            min_distance = end.distance
            actions = []

            while end.predecessor:
                actions.insert(0,end.key)
                end = end.predecessor
            actions.insert(0, end.key)

    print("minimum steps: %s\n%s" % (min_distance, actions))

    return (min_distance, actions)


def build_graph(big, small):
    g = Graph()

    all_states = [(b, s) for b in range(big + 1) for s in range(small + 1)]

    def get_adjacent(b, s):
        res = []

        if b != big:
            res.append((big, s))

        if s != small:
            res.append((b, small))

        if b != 0:
            res.append((0, s))

        if s != 0:
            res.append((b, 0))

        if b + s >= big:
            res.append((big, s - (big - b)))

        if b + s >= small:
            res.append((b - (small - s), small))

        if s != 0:
            res.append((min(big, b + s), 0))

        if b != 0:
            res.append((0, min(small, b + s)))

        return res

    for state in all_states:
        for adj in get_adjacent(*state):
            g.add_edge(state, adj)

    return g


def BFS(graph, start):

    queue = deque()
    start_vertex = graph.get_vertex(start)
    start_vertex.color = 'gray'
    start_vertex.distance = 0
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


water_jug(4, 3, 2)