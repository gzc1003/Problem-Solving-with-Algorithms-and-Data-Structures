from collections import deque

from Graph import Graph


def cross_river(missionaries, cannibals, side):
    g = build_graph(missionaries, cannibals)
    if side == 'Left':
        start = g.get_vertex((0,0,'Left'))
        end = g.get_vertex((missionaries,cannibals,'Right'))
    else:
        start = g.get_vertex((missionaries,cannibals,'Right'))
        end = g.get_vertex((0,0,'Left'))

    BFS(g, start)

    states = []
    while end.predecessor:
        states.insert(0, end.key)
        end = end.predecessor
    states.insert(0, end.key)

    print(states)

    return states


def build_graph(missionaries, cannibals):
    g = Graph()

    all_states = [(m, c, side) for m in range(missionaries + 1) for c in range(cannibals+1) for side in ['Right', 'Left']]
    for state in all_states:
        for adj in get_adj(*state):
            g.add_edge(state, adj)

    return g


def get_adj(m, c, side):
    l_to_r = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]
    r_to_l = [(-2, 0), (0, -2), (-1, -1), (-1, 0), (0, -1)]

    if side == 'Left':
        res = [(m + i, c + j, 'Right') for i, j in l_to_r if is_legal(m + i, c + j)]

    elif side == 'Right':
        res = [(m + i, c + j, 'Left') for i, j in r_to_l if is_legal(m + i, c + j)]

    return res


def is_legal(m, c):
    res = True
    if m < 0 or c < 0 or m >3 or c > 3:
        res = False
    elif 0 < m < c or 0 < 3-m < 3-c:
        res = False

    return res



def BFS(graph, start):
    queue = deque()
    start.color = 'gray'
    start.distance = 0
    queue.append(start)

    while queue:
        current = queue.popleft()
        for adj in current.get_connections():
            if adj.color == 'white':
                adj.color = 'gray'
                adj.predecessor = current
                adj.distance = current.distance + 1
                queue.append(adj)
        current.color = 'black'

cross_river(3, 3, 'Right')