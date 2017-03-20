def n_queen(n):
    row = 0
    all = []
    queens = []
    n_queen_helper(row, n, all, queens)

    return [['.' * coord[1] + 'Q' + '.' * (n - coord[1] - 1) for coord in solution] for solution in all]


def n_queen_helper(row, n, all, queens):
    if row == n:
        all.append(queens)
        return

    position = [(row, column) for column in range(n)]

    for coord in position:
        if is_valid(coord, queens):
            n_queen_helper(row + 1, n, all, queens + [coord])


def is_valid(coord1, queens):
    for coord2 in queens:
        if (coord1[1] == coord2[1]
            or coord1[0] + coord1[1] == coord2[0] + coord2[1]
            or coord1[0] - coord1[1] == coord2[0] - coord2[1]):
            return False
    return True


print(n_queen(4))
