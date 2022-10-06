from turtle import forward, right, left
from turtle import shape, exitonclick

shape("turtle")

prvni = 25
a = 0
for _ in range(19):
    left(90)
    forward(prvni + a)
    a = prvni + a
    
exitonclick()