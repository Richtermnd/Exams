from turtle import *


SCALE = 30

tracer(0)
screensize(2000, 2000)

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
    for _ in range(15):
        move(10, 10)
        move(3, -6)
        move(-9, 3)
    draw_grid()
    update()
    mainloop()


main()
