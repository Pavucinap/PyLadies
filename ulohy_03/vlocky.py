from sys import builtin_module_names
from turtle import back, forward, right, left, backward
from turtle import penup, pendown
from turtle import shape, exitonclick
from turtle import stamp, color

shape("turtle")

penup()
backward(400)
pendown()
color("blue")

backward(20)
right(120)
backward(20)
forward(20)
right(120)
backward(20)
forward(20)

right(120)
backward(25)
left(120)

for _ in range(5):
    backward(45)
    forward(20)
    right(120)
    forward(20)
    backward(20)
    right(120)
    forward(20)
    backward(20)

    right(120)
    forward(25)
    right(60)




exitonclick()
