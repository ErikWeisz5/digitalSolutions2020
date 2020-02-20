import turtle

def rectangle(height, width, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

rectangle(50, 250, "red") # bottom red

turtle.left(90)     #
turtle.forward(50)  # go 50 pixel up
turtle.right(90)    #

rectangle(50, 250, "white") # middle white

turtle.left(90)     #
turtle.forward(50)  # go 50 pixel up
turtle.right(90)    #

rectangle(50, 250, "red") # top red

turtle.done()