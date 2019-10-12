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

def rhombus(x,y,a,b):
    # TODO: (Nikita) Draw rhombus
    turtle.up()
    turtle.setposition(x,y)
    turtle.down()
    turtle.pencolor()
    turtle.forward(a)
    turtle.left(45)
    turtle.forward(b)
    turtle.left(135)
    turtle.forward(a)
    turtle.left(45)
    turtle.forward(b)
    turtle.left(135)
    pass
