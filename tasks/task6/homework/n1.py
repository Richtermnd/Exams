from turtle import *


SCALE = 20

tracer(0)


def draw_grid():
    up()
    for x in range(-20, 20):
        for y in range(-20, 20):
            goto(x * SCALE, y * SCALE)
            dot(4, 'red')


def move(x, y):
    goto(xcor() + x * SCALE, ycor() + y * SCALE)


def main():
    
    draw_grid()
    update()
    mainloop()


main()
