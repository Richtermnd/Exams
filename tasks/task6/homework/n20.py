from turtle import *
import math

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
    cnt = 0
    for x in range(-50, 0):
        for y in range(50):
            cond1 = y > x * -math.tan(math.radians(30))
            cond2 = y < x * math.tan(math.radians(30)) + 30
            cond3 = x < 0
            if cond1 and cond2 and cond3:
                cnt += 1
    print(cnt)


main()
