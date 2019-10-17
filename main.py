# Case 1

# Developers:   Nikita Beushev ()
#               Alexandra Kozadeeva ()
#               Anzhelika Kurepova ()

import turtle
import math

def square(x, y, a, color):
    #TODO: (Alexandra) square
    turtle.showturtle()
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()
    pass

def triangle(x,y,size,color,angle):
    #TODO: (Anzhelika) triangle
    turtle.showturtle()
    turtle.up()
    turtle.setposition(x, y)
    turtle.right(angle)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(135)
    turtle.forward(size * math.sqrt(2))
    turtle.end_fill()
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


def main():
    square(-100, 0, 150, 'brown')
    square(-70, -30, 50, 'red')
    turtle.mainloop()


if __name__ == '__main__':
    main()