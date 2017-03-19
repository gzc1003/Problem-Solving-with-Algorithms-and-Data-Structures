# Write a program to solve the following problem: You have two jugs: a 4-gallon
# jug and a 3-gallon jug. Neither of the jugs have markings on them. There is
# a pump that can be used to fill the jugs with water. How can you get
# exactly two gallons of water in the 4-gallon jug?

# Generalize the problem above so that the parameters to your solution
# includemthe sizes of each jug and the final amount of water to be left in
# the larger jug.



def fill_jugs(small, large, final):
    min_steps = range(1000)
    def helper(s, l, steps):
        nonlocal min_steps
        if (s, l) in steps:
            return False

        if l == final:
            if len(steps+[(s,l)]) < len(min_steps):
                min_steps = steps+[(s,l)]
            return

        actions = [
                   (s, 0),
                   (0, l),
                   (small, l),
                   (s, large),
                   (s - (min(large,l+s) - l), min(large,l+s)),
                   (min(small, s+l), l - (min(small, s+l)-s)),
                  ]

        for new_s, new_l in actions:
            helper(new_s, new_l, steps+[(s, l)])

    helper(small, large, [])
    return min_steps

print(fill_jugs(3,4,2))


