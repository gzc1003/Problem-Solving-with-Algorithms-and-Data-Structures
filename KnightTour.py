from Graph import Graph


def islegal(row, column, bdsize):
    if 0 <= row < bdsize and 0 <= column < bdsize:
        return True
    else:
        return False


def next_move(row, column, bdsize):
    possible_move = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
                     (1, 2), (2, 1), (2, -1), (1, -2)]
    nlist = []
    for move in possible_move:
        if islegal(row + move[0], column + move[1], bdsize):
            nlist.append((row + move[0], column + move[1]))

    return nlist


def build_graph(bdsize):
    g = Graph()
    for row in range(bdsize):
        for column in range(bdsize):
            nlist = next_move(row, column, bdsize)
            for new_node in nlist:
                g.add_edge((row, column), new_node)
    return g


def least_connections(vertex):
    nlist = []
    for nvertex in vertex.get_connections():
        count = 0

        for vert in nvertex.get_connections():
            if vert.color == 'white':
                count += 1

        nlist.append((count, nvertex))
    nlist.sort(key=lambda x: x[0])
    return [item[1] for item in nlist]


def DFS(vertex, path, limit):
    done = False
    path.append(vertex)
    vertex.color = 'gray'

    if len(path) < limit:
        for nvertex in least_connections(vertex):
            if done:
                break
            if nvertex.color == 'white':
                done = DFS(nvertex, path, limit)

        if not done:
            vertex.color = 'white'
            path.pop()
    else:
        done = True
    return done


g = build_graph(8)
path = []
DFS(g.get_vertex((0, 0)), path, 64)

for vertex in path:
    print(vertex.key)
