def searchFrom(maze, startRow, startColumn):
    queue = []
    queue.append((startRow, startColumn))

    while queue:
        coord = queue.pop(0)
        row = coord[0]
        col = coord[1]
        maze.updatePosition(row, col)
        maze.updatePosition(row, col, TRIED)
        connections = [adj for adj in [(row-1,col), (row+1,col), (row,col-1), (row,col+1)] if isleagal(adj, maze)]
        for adj in connections:
            if maze[adj[0]][adj[1]] == ' ':
                queue.append((adj[0],adj[1]))
                maze[adj[0]][adj[1]] = (row, col)

    coord = (2,0)
    while maze[coord[0]][coord[1]] != 'S':
        row = coord[0]
        col = coord[1]
        maze.updatePosition(row, col, PART_OF_PATH)
        coord = maze[coord[0]][coord[1]]
    maze.updatePosition(coord[0], coord[1], PART_OF_PATH)



def isleagal(coord, maze):
    res = False
    if 0 <= coord[0] < maze.rowsInMaze and \
        0 <= coord[1] < maze.columnsInMaze:
        res = True
    return res




