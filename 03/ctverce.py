from turtle import forward, right, left
from turtle import shape, exitonclick

shape("turtle")

for _ in range(18):     # 18 opakování cyklu pod; _ nahrazuje proměnnou, když se nemusí specifikovat
    left(20)            # otočení o 20
    for _ in range(4):  # opakování pohybu pod prvním for
        forward(200)
        right(90)
   
exitonclick()