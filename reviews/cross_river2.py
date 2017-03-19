# Write a program that solves the following problem: Three missionaries and
# three cannibals come to a river and find a boat that holds two people.
# Everyone must get across the river to continue on the journey. However,
# if the cannibals ever outnumber the missionaries on either bank,
# the missionaries will be eaten. Find a series of crossings that will get
# everyone safely to the other side of the river.


def cross_river(missionaries, cannibals):
    return helper(missionaries, cannibals, missionaries, cannibals, 'R', [])


def helper(missionaries, cannibals, right_m, right_c, boat, states):
    if (right_m != 0 and right_m < right_c) or (
                        missionaries - right_m != 0 and missionaries - right_m < cannibals - right_c):
        return False
    if (right_m, right_c, boat) in states:
        return False
    if right_m == 0 and right_c == 0:
        return states + [(right_m, right_c, boat)]

    if boat == 'R':
        actions = [(-1, -1), (-1, 0), (0, -1), (-2, 0), (0, -2)]
        new_boat = 'L'
    else:
        actions = [(1, 1), (1, 0), (0, 1), (2, 0), (0, 2)]
        new_boat = 'R'

    for m, c in actions:
        if 0 <= right_m + m <= missionaries and 0 <= right_c + c <= cannibals:
            res = helper(missionaries, cannibals, right_m + m, right_c + c,
                      new_boat, states + [(right_m, right_c, boat)])
            if res:
                return res
    return False


print(cross_river(3, 3))
