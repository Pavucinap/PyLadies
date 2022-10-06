from turtle import forward, right, left
from turtle import shape, exitonclick

shape("turtle")

n = 100
strana = 500 / n
uhel = 180 - (180 * (1 - 2/n))
for _ in range(n):
    forward(strana)
    left(uhel)
    
exitonclick()