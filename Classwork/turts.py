import turtle
turtle.showturtle()
var = 270
t = turtle
t.setup(1080, 720)


def star7():
    t.pencolor('white')
    angle = 180.0 - 180.0 / 7
    t.bgcolor('blue')
    turtle.speed(12)
    t.fillcolor('white')
    t.begin_fill()
    for x in range(7):
        t.forward(30)
        t.right(angle)
    t.end_fill()

star7()
t.penup()
t.goto(180, -60)
t.pendown()
star7()
t.penup()
t.goto(3, -260)
t.left(90)
t.pendown()
star7()
t.penup()
t.right(180)
t.goto(180, -200)
t.pendown()
star7()
turtle.done()
