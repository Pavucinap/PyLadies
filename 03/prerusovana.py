from turtle import forward, pendown, right, left
from turtle import penup; pendown
from turtle import shape, exitonclick


shape("turtle")

delka = 10
for i in range(1, 10):
   pendown()
   forward(i * delka)
   penup()
   forward(10)
   
exitonclick()