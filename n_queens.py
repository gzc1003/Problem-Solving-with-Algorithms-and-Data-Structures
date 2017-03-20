def n_queen(n):
    row = 0
    all = []
    queens = []
    res = []
    n_queen_helper(row, n, all, queens)


    for one_solution in all:
        chessboard = [['.'] * n for i in range(n)]
        newboard = []
        for coord in one_solution:
            chessboard[coord[0]][coord[1]] = 'Q'
        for row in chessboard:
            newboard.append(''.join(row))
        res.append(newboard)
    return res

def n_queen_helper(row,n,all,queens):
    position = [(row, column) for column in range(n)]
    for coord in position:
        placed = True
        for queen in queens:
            if not is_valid(coord, queen):
                placed = False
                break
        if placed:
            queens.append(coord)
            if row == n-1:
                all.append(list(queens))
            else:
                n_queen_helper(row+1, n, all, queens)
            queens.pop()


def is_valid(coord1, coord2):
    if (coord1[1] == coord2[1] or
        coord1[0] + coord1[1] == coord2[0] + coord2[1] or
        coord1[0] - coord1[1] == coord2[0] - coord2[1]):
        return False
    else:
        return True

print(n_queen(4))