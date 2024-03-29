# Case 1
# Developers:   Nikita Beushev (70%)
#               Alexandra Kozadeeva (60%)
#               Anzhelika Kurepova (55%)

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


def circle (x, y, radius, line_color, fill_color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.pencolor(line_color)
    turtle.fillcolor(fill_color)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def line(x, y, length, angle, line_color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.setheading(angle)
    turtle.pencolor(line_color)
    turtle.down()
    turtle.forward(length)


def ship():
    rhombus(-174, 100, 75, 75, 135, 'brown', 'brown')
    triangle(-118, 153,75,225,'salmon4','salmon4')
    triangle(-200, 155, 50, 45, 'gray93', 'white smoke')
    triangle(-200, 300, 100, 315, 'gray93', 'ghost white')
    triangle(-202, 255, 100, 270, 'gray93', 'snow')
    triangle(-150, 303, 50, 180, 'black', 'black')
    square(-163, 192,50,45,'gray93','gray95')


def fish():
    rhombus(223, 101, 75, 50, 135, 'sky blue', 'sky blue')
    square(225, 100, 50, 45, 'royal blue', 'royal blue')
    triangle(299, 135, 50, 315, 'powder blue', 'powder blue')
    triangle(297, 98, 75, 270, 'blue', 'blue')
    triangle(222, 177, 75, 0, 'deep sky blue', 'deep sky blue')
    triangle(171, 99, 50, 270, 'steel blue', 'steel blue')
    triangle(173, 49, 50, 90, 'light steel blue', 'light steel blue')


def hare():
    rhombus(100, -50, 70, 50, 135, 'black', 'green')
    square(65, -50, 50, 0, 'black', 'orange')
    triangle(65, -75, 80, 270, 'black', 'red')
    triangle(-15, -235, 80, 90, 'black', 'yellow')
    triangle(65, -130, 40, 315, 'black', 'pink')
    triangle(45, -175, 60, 270, 'black', 'blue')
    triangle(85, -235, 40, 180, 'black', 'purple')


def deer():
    rectangle(90, 320, 15, 80, 0, 'black', 'yellow')
    circle(100, 300, 30, '', 'orange')
    circle(110, 295, 30, '', 'orange')
    triangle(83, 353, 15, 60, 'black', 'brown')
    triangle(95, 355, 15, 50, 'black', 'brown')
    rhombus(105, 190, 70, 115, 135, 'black', 'brown')
    triangle(55, 240, 50, 0, 'black', 'yellow')
    rectangle(75, 190, 10, 80, 0, 'black', 'yellow')
    rectangle(65, 190, 10, 80, 0, 'black', 'yellow')
    rectangle(0, 190, 10, 80, 0, 'black', 'brown')
    rectangle(-10, 190, 10, 80, 0, 'black', 'brown')
    triangle(-57, 240, 20, 270, 'black', 'brown')


def rocket():
    triangle(-200, -50, 50, 45, 'white', 'purple')
    triangle(-200, -120, 70, 90, 'white', 'lightblue')
    triangle(-128, -190, 97, 135, 'white', 'red')
    triangle(-200, -121, 96, 315, 'white', 'yellow')
    square(-165, -225, 50, 45, 'white', 'orange')
    triangle(-95, -295, 50, 135, 'white', 'purple')
    rhombus(-235, -290, 50, 70, 45, 'white', 'green')


def pep_love():
    circle (-300, -250, 100, 'white', 'red')
    circle(-315, -240, 80, 'white', 'white')
    circle (-320, -80, 50, 'white', 'red')
    circle(-335, -70, 30, 'white', 'white')
    rectangle(-420, -187, 53, 100, 90, 'white', 'black')
    line(-380, -140, 20, 0, 'pink')
    line(-380, -160, 20, 0, 'pink')
    line(-380, -180, 20, 0, 'pink')
    line(-380, -180, 40, 90, 'pink')
    line(-410, -180, 40, 90, 'pink')
    line(-410, -160, 14, 45, 'pink')
    line(-410, -140, 14, 315, 'pink')
    line(-340, -180, 40, 90, 'pink')
    line(-340, -160, 14, 45, 'pink')
    line(-340, -140, 14, 315, 'pink')
    triangle(-500, -121, 26, 45, 'white', 'pink')
    triangle(-497, -155, 33, 90, 'white', 'purple')
    triangle(-495, -154, 40, 135, 'white', 'red')
    rectangle(-500, -150, 9, 80, 0, 'white', 'green')
    triangle(-500, -194, 20, 135, 'white', 'green')
    rhombus(-513, -180, 15, 20, 45, 'white', 'lightgreen')
    triangle(-491, -194, 10, 315, 'white', 'green')
    triangle(-260, -51, 26, 45, 'white', 'pink')
    triangle(-257, -85, 33, 90, 'white', 'purple')
    triangle(-255, -84, 40, 135, 'white', 'red')
    triangle(-470, -31, 26, 45, 'white', 'pink')
    triangle(-467, -65, 33, 90, 'white', 'purple')
    triangle(-465, -64, 40, 135, 'white', 'red')


def main():
    turtle.speed(0)
    turtle.hideturtle()
    ship()
    fish()
    hare()
    deer()
    rocket()
    pep_love()
    turtle.mainloop()


if __name__ == '__main__':
    main()


