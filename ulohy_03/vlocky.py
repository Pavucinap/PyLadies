from turtle import back, forward, right, left, backward, goto, penup, pendown, shape, exitonclick, stamp, color, pensize
from random import randrange

shape("circle")



for _ in range(randrange(5,15)):
    penup()
    left(randrange(0, 360))
    goto(randrange(-250, 250),randrange(-250, 250))
    pendown()
    
    n = randrange(1, 5)
        
    if n > 3:
        color("blue")
        pensize(5)
    elif n > 1:
        color("dodgerblue1")
        pensize(3)
    else:
        color("cadetblue2")
        pensize(1)

    for _ in range(6):
        backward(n * 30)
        forward(n * 10)
        for _ in range(2):
            right(120)
            forward(n * 4)
            backward(n * 4)
        
        right(120)
        forward(n * 5)
        for _ in range(2):
            right(120)
            forward(n * 10)
            backward(n * 10)
        right(120)
        forward(n * 15)
        right(60)

    stamp()

exitonclick()
