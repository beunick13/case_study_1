# Case 1

# Developers:   Nikita Beushev ()
#               Alexandra Kozadeeva ()
#               Anzhelika Kurepova ()

import turtle

def square(x,y,a,color,angle):
    #TODO: (Alexandra) square
    turtle.showturtle()
    turtle.down()
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    pass

def triangle(x,y,a,color):
    #TODO: (Anzhelika) triangle
    pass


def rhombus(x, y, a, b, color):
    # TODO: (Nikita) Draw rhombus
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.up()
    turtle.setposition(x,y)
    turtle.down()
    turtle.beginfill()
    turtle.forward(a)
    turtle.left(45)
    turtle.forward(b)
    turtle.left(135)
    turtle.forward(a)
    turtle.left(45)
    turtle.forward(b)
    turtle.left(135)
    turtle.end_fill()
    pass

def circles (x, y, radius, colour):
turtle.up()
turtle.setposition(x, y)
turtle.down()
turtle.fillcolor(colour)
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()