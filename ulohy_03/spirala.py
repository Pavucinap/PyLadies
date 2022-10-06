from turtle import forward, right, left
from turtle import shape, exitonclick

shape("turtle")

n = 100
prvni = 1 / n
uhel = 180 - (180 * (1 - 2/n))
a = 0
for _ in range(n * 17):
    left(uhel)
    forward(prvni + a)
    a = prvni + a
    
exitonclick()