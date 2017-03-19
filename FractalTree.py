import turtle
import random


def tree(branchlen, t:turtle.Turtle, width):
    if branchlen > 5:
        width -= 0.4
        t.pen(pensize=width, pencolor='green')
        t.forward(branchlen)
        angle = random.randrange(15,46)
        t.right(angle)
        tree(branchlen-random.randrange(10,20), t, width)
        t.left(2*angle)
        tree(branchlen-random.randrange(10,20), t, width)
        t.right(angle)
        t.backward(branchlen)


t = turtle.Turtle()
mywin = turtle.Screen()
t.left(90)
t.up()
t.backward(100)
t.down()
width = 5
tree(100,t,width)
mywin.exitonclick()