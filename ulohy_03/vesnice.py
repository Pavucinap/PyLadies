from turtle import forward, right, left
from turtle import shape, exitonclick

shape("turtle")

strana = 100
for _ in range(5):
    forward(strana)
    left(135)
    forward(strana * 2**(1/2))
    left(135)
    forward(strana)
    left(135)
    forward(strana * 2**(1/2))
    left(135)
    forward(strana)
    right(135)
    forward((strana / 2) * 2**(1/2))
    right(90)
    forward((strana / 2) * 2**(1/2))
    right(45)
    forward(strana)
    left(90)
    forward(10)

exitonclick()