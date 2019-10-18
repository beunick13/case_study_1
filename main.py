# Case 1

# Developers:   Nikita Beushev ()
#               Alexandra Kozadeeva ()
#               Anzhelika Kurepova ()

import turtle
import math


def square(x, y, a, angle, line_color, fill_color):
    #TODO: (Alexandra) square
    turtle.up()
    turtle.setposition(x, y)
    turtle.setheading(angle)
    turtle.pencolor(line_color)
    turtle.fillcolor(fill_color)
    turtle.down()
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


def triangle(x, y, size, angle, line_color, fill_color):
    #TODO: (Anzhelika) triangle
    turtle.up()
    turtle.setposition(x, y)
    turtle.setheading(angle)
    turtle.pencolor(line_color)
    turtle.fillcolor(fill_color)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(135)
    turtle.forward(size * math.sqrt(2))
    turtle.end_fill()
    pass


def rhombus(x, y, length, height, angle, line_color, fill_color):
    # TODO: (Nikita) Draw rhombus
    turtle.up()
    turtle.setposition(x, y)
    turtle.setheading(angle)
    turtle.pencolor(line_color)
    turtle.fillcolor(fill_color)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(length)
    turtle.left(45)
    turtle.forward(height)
    turtle.left(135)
    turtle.forward(length)
    turtle.left(45)
    turtle.forward(height)
    turtle.left(135)
    turtle.end_fill()
    pass


def circle (x, y, radius, line_color, fill_color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.pencolor(line_color)
    turtle.fillcolor(fill_color)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    pass


def line(x, y, length, angle, line_color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.setheading(angle)
    turtle.pencolor(line_color)
    turtle.down()
    turtle.forward(length)
    pass


def picture_1():
    # 1x1
    # -450, 150
    # Nikita
    rhombus(-450,150, 50, 100, 35, 'red', 'blue')
    pass


def picture_2():
    # 1x2
    # -150, 150
    # Nikita
    pass


def picture_3():
    # 1x3
    # 150, 150
    # Nikita
    pass


def picture_4():
    # 2x1
    # -450, -150
    # Anzhelika
    pass


def picture_5():
    # 2x2
    # -150, -150
    # Anzhelika
    pass


def picture_6():
    # 2x3
    # 150, -150
    # Anzhelika
    pass


def picture_7():
    # 3x1
    # -450, -450
    # Alexandra
    pass


def picture_8():
    # 3x2
    # -150, -450
    # Alexandra
    pass


def picture_9():
    # 3x3
    # 150, -450
    # Alexandra
    pass


def main():
    turtle.setup(900, 900)
    turtle.speed(0)
    turtle.hideturtle()
    picture_1()
    picture_2()
    picture_3()
    picture_4()
    picture_5()
    picture_6()
    picture_7()
    picture_8()
    picture_9()
    turtle.mainloop()


if __name__ == '__main__':
    main()


