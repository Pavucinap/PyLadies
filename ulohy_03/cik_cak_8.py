from turtle import forward, right, left
from turtle import shape, exitonclick

shape("turtle")

prvni = 2
a = 0
for _ in range(59):
    left(45)
    forward(prvni + a)
    a = prvni + a
    
exitonclick()