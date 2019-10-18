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
def rectangle(x, y, a, b, angle, line_color, fill_color):
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
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
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
    pass

def picture_6():
    circle (-300, -250, 100, 'white', 'red')
    circle(-310, -240, 80, 'white', 'white')
    circle (-320, -80, 50, 'white', 'red')
    circle(-330, -70, 30, 'white', 'white')
    rectangle(-410, -167, 53, 100, 90, 'white', 'black')
    line(-370, -120, 20, 0, 'pink')
    line(-370, -140, 20, 0, 'pink')
    line(-370, -160, 20, 0, 'pink')
    line(-370, -160, 40, 90, 'pink')
    line(-400, -160, 40, 90, 'pink')
    line(-400, -140, 14, 45, 'pink')
    line(-400, -120, 14, 315, 'pink')
    line(-330, -160, 40, 90, 'pink')
    line(-330, -140, 14, 45, 'pink')
    line(-330, -120, 14, 315, 'pink')
    rhombus(1, 1, 10, 5, 0, 'white', 'black')
    triangle(-200, -50, 50, 45, 'white', 'purple')
    triangle(-200, -120, 70, 90, 'white', 'lightblue')
    triangle(-128, -190, 97, 135, 'white', 'red')
    triangle(-200, -121, 96, 315, 'white', 'yellow')
    square(-165, -225, 50, 45, 'white', 'orange')
    triangle(-95, -295, 50, 135, 'white', 'purple')
    rhombus(-235, -290, 50, 70, 45, 'white', 'green')
    pass

def main():

    turtle.speed(0)
    turtle.hideturtle()
    picture_1()
    picture_2()
    picture_3()
    picture_4()
    picture_5()
    picture_6()

    turtle.mainloop()


if __name__ == '__main__':
    main()


