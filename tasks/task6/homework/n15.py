from turtle import *


SCALE = 20

tracer(0)


def draw_grid():
    up()
    for x in range(-20, 20):
        for y in range(-20, 20):
            goto(x * SCALE, y * SCALE)
            dot(4, 'red')


def draw_axis():
    up()
    goto(-20 * SCALE, 0 * SCALE)
    down()
    goto(20 * SCALE, 0 * SCALE)
    
    up()
    goto(0 * SCALE, -20 * SCALE)
    down()
    goto(0 * SCALE, 20 * SCALE)


def move(x, y):
    goto(xcor() + x * SCALE, ycor() + y * SCALE)


def main():
    lt(90)
    for _ in range(5):
        move(5, 4)
        move(4, -4)
        move(-7, -2)
        move(-2, 2)
    draw_grid()
    update()
    mainloop()


main()
