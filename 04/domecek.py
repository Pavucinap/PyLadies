from turtle import fillcolor, begin_fill, forward, left, end_fill, exitonclick

size = 100
color = "yellow"

#Nastavení barvy
fillcolor(color)
begin_fill()

# Nakreslí šestiúhelník
for _ in range(6):
    forward(size)
    left(60)

end_fill()

exitonclick()